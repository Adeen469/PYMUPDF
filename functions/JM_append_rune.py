"""
Function: fitz.JM_append_rune
Signature: JM_append_rune(buff, ch)
Description:
APPEND non-ascii runes in unicode escape format to fz_buffer.
"""

import fitz

# Source code of fitz.JM_append_rune:
def JM_append_rune(buff, ch):
    """
    APPEND non-ascii runes in unicode escape format to fz_buffer.
    """
    mupdf.fz_append_string(buff, make_escape(ch))
