"""
Function: fitz.JM_get_annot_by_xref
Signature: JM_get_annot_by_xref(page, xref)
Description:
retrieve annot by its xref
"""

import fitz

# Source code of fitz.JM_get_annot_by_xref:
def JM_get_annot_by_xref(page, xref):
    '''
    retrieve annot by its xref
    '''
    assert isinstance(page, mupdf.PdfPage)
    found = 0
    # loop thru MuPDF's internal annots array
    annot = mupdf.pdf_first_annot(page)
    while 1:
        if not annot.m_internal:
            break
        if xref == mupdf.pdf_to_num(mupdf.pdf_annot_obj(annot)):
            found = 1
            break
        annot = mupdf.pdf_next_annot( annot)
    if not found:
        raise Exception("xref %d is not an annot of this page" % xref)
    return annot
