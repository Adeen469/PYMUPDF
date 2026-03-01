"""
Function: fitz.util_sine_between
Signature: util_sine_between(C, P, Q)
Description: No docstring available.
"""

import fitz

# Source code of fitz.util_sine_between:
def util_sine_between(C, P, Q):
    # for points C, P, Q compute the sine between lines CP and QP
    c = JM_point_from_py(C)
    p = JM_point_from_py(P)
    q = JM_point_from_py(Q)
    s = mupdf.fz_normalize_vector(mupdf.fz_make_point(q.x - p.x, q.y - p.y))
    m1 = mupdf.fz_make_matrix(1, 0, 0, 1, -p.x, -p.y)
    m2 = mupdf.fz_make_matrix(s.x, -s.y, s.y, s.x, 0, 0)
    m1 = mupdf.fz_concat(m1, m2)
    c = mupdf.fz_transform_point(c, m1)
    c = mupdf.fz_normalize_vector(c)
    return c.y
