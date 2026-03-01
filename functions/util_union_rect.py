"""
Function: fitz.util_union_rect
Signature: util_union_rect(r1, r2)
Description: No docstring available.
"""

import fitz

# Source code of fitz.util_union_rect:
def util_union_rect( r1, r2):
    return JM_py_from_rect(
            mupdf.fz_union_rect(
                JM_rect_from_py(r1),
                JM_rect_from_py(r2),
                )
            )
