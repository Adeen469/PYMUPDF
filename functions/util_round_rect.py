"""
Function: fitz.util_round_rect
Signature: util_round_rect(rect)
Description: No docstring available.
"""

import fitz

# Source code of fitz.util_round_rect:
def util_round_rect( rect):
    return JM_py_from_irect(mupdf.fz_round_rect(JM_rect_from_py(rect)))
