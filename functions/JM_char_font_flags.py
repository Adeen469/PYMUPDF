"""
Function: fitz.JM_char_font_flags
Signature: JM_char_font_flags(font, line, ch)
Description: No docstring available.
"""

import fitz

# Source code of fitz.JM_char_font_flags:
def JM_char_font_flags(font, line, ch):
    flags = 0
    if line and ch:
        flags += detect_super_script(line, ch)
    flags += mupdf.fz_font_is_italic(font) * TEXT_FONT_ITALIC
    flags += mupdf.fz_font_is_serif(font) * TEXT_FONT_SERIFED
    flags += mupdf.fz_font_is_monospaced(font) * TEXT_FONT_MONOSPACED
    flags += mupdf.fz_font_is_bold(font) * TEXT_FONT_BOLD
    return flags
