"""
Function: fitz.JM_is_rtl_char
Signature: JM_is_rtl_char(ch)
Description: No docstring available.
"""

import fitz

# Source code of fitz.JM_is_rtl_char:
def JM_is_rtl_char(ch):
    if ch < 0x590 or ch > 0x900:
        return False
    return True
