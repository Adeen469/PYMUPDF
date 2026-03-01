"""
Function: fitz.page_merge
Signature: page_merge(doc_des, doc_src, page_from, page_to, rotate, links, copy_annots, graft_map)
Description:
Deep-copies a source page to the target.
Modified version of function of pdfmerge.c: we also copy annotations, but
we skip some subtypes. In addition we rotate output.
"""

import fitz

# Source code of fitz.page_merge:
def page_merge(doc_des, doc_src, page_from, page_to, rotate, links, copy_annots, graft_map):
    '''
    Deep-copies a source page to the target.
    Modified version of function of pdfmerge.c: we also copy annotations, but
    we skip some subtypes. In addition we rotate output.
    '''
    if g_use_extra:
        #log( 'Calling C++ extra.page_merge()')
        return extra.page_merge( doc_des, doc_src, page_from, page_to, rotate, links, copy_annots, graft_map)
    
    # list of object types (per page) we want to copy
    known_page_objs = [
        PDF_NAME('Contents'),
        PDF_NAME('Resources'),
        PDF_NAME('MediaBox'),
        PDF_NAME('CropBox'),
        PDF_NAME('BleedBox'),
        PDF_NAME('TrimBox'),
        PDF_NAME('ArtBox'),
        PDF_NAME('Rotate'),
        PDF_NAME('UserUnit'),
        ]
    page_ref = mupdf.pdf_lookup_page_obj(doc_src, page_from)

    # make new page dict in dest doc
    page_dict = mupdf.pdf_new_dict(doc_des, 4)
    mupdf.pdf_dict_put(page_dict, PDF_NAME('Type'), PDF_NAME('Page'))

    # copy objects of source page into it
    for i in range( len(known_page_objs)):
        obj = mupdf.pdf_dict_get_inheritable( page_ref, known_page_objs[i])
        if obj.m_internal:
            #log( '{=type(graft_map) type(graft_map.this)}')
            mupdf.pdf_dict_put( page_dict, known_page_objs[i], mupdf.pdf_graft_mapped_object(graft_map.this, obj))

    # Copy annotations, but skip Link, Popup, IRT, Widget types
    # If selected, remove dict keys P (parent) and Popup
    if copy_annots:
        old_annots = mupdf.pdf_dict_get( page_ref, PDF_NAME('Annots'))
        n = mupdf.pdf_array_len( old_annots)
        if n > 0:
            new_annots = mupdf.pdf_dict_put_array( page_dict, PDF_NAME('Annots'), n)
            for i in range(n):
                o = mupdf.pdf_array_get( old_annots, i)
                if not o.m_internal or not mupdf.pdf_is_dict(o):
                    continue    # skip non-dict items
                if mupdf.pdf_dict_gets( o, "IRT").m_internal:
                    continue
                subtype = mupdf.pdf_dict_get( o, PDF_NAME('Subtype'))
                if mupdf.pdf_name_eq( subtype, PDF_NAME('Link')):
                    continue
                if mupdf.pdf_name_eq( subtype, PDF_NAME('Popup')):
                    continue
                if mupdf.pdf_name_eq(subtype, PDF_NAME('Widget')):
                    continue
                mupdf.pdf_dict_del( o, PDF_NAME('Popup'))
                mupdf.pdf_dict_del( o, PDF_NAME('P'))
                copy_o = mupdf.pdf_graft_mapped_object( graft_map.this, o)
                annot = mupdf.pdf_new_indirect( doc_des, mupdf.pdf_to_num( copy_o), 0)
                mupdf.pdf_array_push( new_annots, annot)

    # rotate the page
    if rotate != -1:
        mupdf.pdf_dict_put_int( page_dict, PDF_NAME('Rotate'), rotate)
    # Now add the page dictionary to dest PDF
    ref = mupdf.pdf_add_object( doc_des, page_dict)

    # Insert new page at specified location
    mupdf.pdf_insert_page( doc_des, page_to, ref)
