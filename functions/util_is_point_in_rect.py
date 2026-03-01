"""
Function: fitz.util_is_point_in_rect
Signature: util_is_point_in_rect(p, r)
Description: No docstring available.
"""

import fitz

# Source code of fitz.util_is_point_in_rect:
def util_is_point_in_rect( p, r):
    return mupdf.fz_is_point_inside_rect(
                JM_point_from_py(p),
                JM_rect_from_py(r),
                )
