"""
Function: fitz.util_transform_point
Signature: util_transform_point(point, matrix)
Description: No docstring available.
"""

import fitz

# Source code of fitz.util_transform_point:
def util_transform_point( point, matrix):
    return JM_py_from_point(
            mupdf.fz_transform_point(
                JM_point_from_py(point),
                JM_matrix_from_py(matrix),
                )
            )
