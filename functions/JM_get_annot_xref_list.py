"""
Function: fitz.JM_get_annot_xref_list
Signature: JM_get_annot_xref_list(page_obj)
Description:
return the xrefs and /NM ids of a page's annots, links and fields
"""

import fitz

# Source code of fitz.JM_get_annot_xref_list:
def JM_get_annot_xref_list( page_obj):
    '''
    return the xrefs and /NM ids of a page's annots, links and fields
    '''
    if g_use_extra:
        names = extra.JM_get_annot_xref_list( page_obj)
        return names
    
    names = []
    annots = mupdf.pdf_dict_get( page_obj, PDF_NAME('Annots'))
    n = mupdf.pdf_array_len( annots)
    for i in range( n):
        annot_obj = mupdf.pdf_array_get( annots, i)
        xref = mupdf.pdf_to_num( annot_obj)
        subtype = mupdf.pdf_dict_get( annot_obj, PDF_NAME('Subtype'))
        if not subtype.m_internal:
            continue    # subtype is required
        type_ = mupdf.pdf_annot_type_from_string( mupdf.pdf_to_name( subtype))
        if type_ == mupdf.PDF_ANNOT_UNKNOWN:
            continue    # only accept valid annot types
        id_ = mupdf.pdf_dict_gets( annot_obj, "NM")
        names.append( (xref, type_, mupdf.pdf_to_text_string( id_)))
    return names
