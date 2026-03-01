"""
Function: fitz.util_point_in_quad
Signature: util_point_in_quad(P, Q)
Description: No docstring available.
"""

import fitz

# Source code of fitz.util_point_in_quad:
def util_point_in_quad( P, Q):
    p = JM_point_from_py(P)
    q = JM_quad_from_py(Q)
    return mupdf.fz_is_point_inside_quad(p, q)
