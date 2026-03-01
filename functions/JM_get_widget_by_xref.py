"""
Function: fitz.JM_get_widget_by_xref
Signature: JM_get_widget_by_xref(page, xref)
Description:
retrieve widget by its xref
"""

import fitz

# Source code of fitz.JM_get_widget_by_xref:
def JM_get_widget_by_xref( page, xref):
    '''
    retrieve widget by its xref
    '''
    found = False
    annot = mupdf.pdf_first_widget( page)
    while annot.m_internal:
        annot_obj = mupdf.pdf_annot_obj( annot)
        if xref == mupdf.pdf_to_num( annot_obj):
            found = True
            break
        annot = mupdf.pdf_next_widget( annot)
    if not found:
        raise Exception( f"xref {xref} is not a widget of this page")
    return Annot( annot)
