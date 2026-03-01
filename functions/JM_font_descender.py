"""
Function: fitz.JM_font_descender
Signature: JM_font_descender(font)
Description:
need own versions of ascender / descender
"""

import fitz

# Source code of fitz.JM_font_descender:
def JM_font_descender(font):
    '''
    need own versions of ascender / descender
    '''
    assert isinstance(font, mupdf.FzFont)
    if _globals.skip_quad_corrections:
        return -0.2
    ret = mupdf.fz_font_descender(font)
    return ret
