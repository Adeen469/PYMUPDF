"""
Function: fitz.util_concat_matrix
Signature: util_concat_matrix(m1, m2)
Description: No docstring available.
"""

import fitz

# Source code of fitz.util_concat_matrix:
def util_concat_matrix( m1, m2):
    return JM_py_from_matrix(
            mupdf.fz_concat(
                JM_matrix_from_py(m1),
                JM_matrix_from_py(m2),
                )
            )
