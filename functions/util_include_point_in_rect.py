"""
Function: fitz.util_include_point_in_rect
Signature: util_include_point_in_rect(r, p)
Description: No docstring available.
"""

import fitz

# Source code of fitz.util_include_point_in_rect:
def util_include_point_in_rect( r, p):
    return JM_py_from_rect(
            mupdf.fz_include_point_in_rect(
                JM_rect_from_py(r),
                JM_point_from_py(p),
                )
            )
