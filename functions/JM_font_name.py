"""
Function: fitz.JM_font_name
Signature: JM_font_name(font)
Description: No docstring available.
"""

import fitz

# Source code of fitz.JM_font_name:
def JM_font_name(font):
    assert isinstance(font, mupdf.FzFont)
    name = mupdf.fz_font_name(font)
    s = name.find('+')
    if _globals.subset_fontnames or s == -1 or s != 6:
        return name
    return name[s + 1:]
