"""
Function: fitz.EMPTY_IRECT
Signature: EMPTY_IRECT()
Description: No docstring available.
"""

import fitz

# Source code of fitz.EMPTY_IRECT:
def EMPTY_IRECT():
    return IRect(FZ_MAX_INF_RECT, FZ_MAX_INF_RECT, FZ_MIN_INF_RECT, FZ_MIN_INF_RECT)
