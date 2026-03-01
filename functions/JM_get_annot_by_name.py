"""
Function: fitz.JM_get_annot_by_name
Signature: JM_get_annot_by_name(page, name)
Description:
retrieve annot by name (/NM key)
"""

import fitz

# Source code of fitz.JM_get_annot_by_name:
def JM_get_annot_by_name(page, name):
    '''
    retrieve annot by name (/NM key)
    '''
    assert isinstance(page, mupdf.PdfPage)
    if not name:
        return
    found = 0
    # loop thru MuPDF's internal annots and widget arrays
    annot = mupdf.pdf_first_annot(page)
    while 1:
        if not annot.m_internal:
            break

        response, len_ = mupdf.pdf_to_string(mupdf.pdf_dict_gets(mupdf.pdf_annot_obj(annot), "NM"))
        if name == response:
            found = 1
            break
        annot = mupdf.pdf_next_annot(annot)
    if not found:
        raise Exception("'%s' is not an annot of this page" % name)
    return annot
