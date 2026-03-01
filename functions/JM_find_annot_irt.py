"""
Function: fitz.JM_find_annot_irt
Signature: JM_find_annot_irt(annot)
Description:
Return the first annotation whose /IRT key ("In Response To") points to
annot. Used to remove the response chain of a given annotation.
"""

import fitz

# Source code of fitz.JM_find_annot_irt:
def JM_find_annot_irt(annot):
    '''
    Return the first annotation whose /IRT key ("In Response To") points to
    annot. Used to remove the response chain of a given annotation.
    '''
    assert isinstance(annot, mupdf.PdfAnnot)
    irt_annot = None    # returning this
    annot_obj = mupdf.pdf_annot_obj(annot)
    found = 0
    # loop thru MuPDF's internal annots array
    page = _pdf_annot_page(annot)
    irt_annot = mupdf.pdf_first_annot(page)
    while 1:
        assert isinstance(irt_annot, mupdf.PdfAnnot)
        if not irt_annot.m_internal:
            break
        irt_annot_obj = mupdf.pdf_annot_obj(irt_annot)
        o = mupdf.pdf_dict_gets(irt_annot_obj, 'IRT')
        if o.m_internal:
            if not mupdf.pdf_objcmp(o, annot_obj):
                found = 1
                break
        irt_annot = mupdf.pdf_next_annot(irt_annot)
    if found:
        return irt_annot
