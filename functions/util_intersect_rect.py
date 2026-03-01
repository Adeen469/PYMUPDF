"""
Function: fitz.util_intersect_rect
Signature: util_intersect_rect(r1, r2)
Description: No docstring available.
"""

import fitz

# Source code of fitz.util_intersect_rect:
def util_intersect_rect( r1, r2):
    return JM_py_from_rect(
            mupdf.fz_intersect_rect(
                JM_rect_from_py(r1),
                JM_rect_from_py(r2),
                )
            )
