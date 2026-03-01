"""
Function: fitz.JM_page_rotation
Signature: JM_page_rotation(page)
Description:
return a PDF page's /Rotate value: one of (0, 90, 180, 270)
"""

import fitz

# Source code of fitz.JM_page_rotation:
def JM_page_rotation(page):
    '''
    return a PDF page's /Rotate value: one of (0, 90, 180, 270)
    '''
    rotate = 0

    obj = mupdf.pdf_dict_get_inheritable( page.obj(), mupdf.PDF_ENUM_NAME_Rotate)
    rotate = mupdf.pdf_to_int(obj)
    rotate = JM_norm_rotation(rotate)
    return rotate
