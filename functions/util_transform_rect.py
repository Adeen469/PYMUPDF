"""
Function: fitz.util_transform_rect
Signature: util_transform_rect(rect, matrix)
Description: No docstring available.
"""

import fitz

# Source code of fitz.util_transform_rect:
def util_transform_rect( rect, matrix):
    if g_use_extra:
        return extra.util_transform_rect( rect, matrix)
    return JM_py_from_rect(mupdf.fz_transform_rect(JM_rect_from_py(rect), JM_matrix_from_py(matrix)))
