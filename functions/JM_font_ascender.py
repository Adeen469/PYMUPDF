"""
Function: fitz.JM_font_ascender
Signature: JM_font_ascender(font)
Description:
need own versions of ascender / descender
"""

import fitz

# Source code of fitz.JM_font_ascender:
def JM_font_ascender(font):
    '''
    need own versions of ascender / descender
    '''
    assert isinstance(font, mupdf.FzFont)
    if _globals.skip_quad_corrections:
        return 0.8
    return mupdf.fz_font_ascender(font)
