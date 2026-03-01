"""
Function: fitz.util_hor_matrix
Signature: util_hor_matrix(C, P)
Description:
Return the matrix that maps two points C, P to the x-axis such that
C -> (0,0) and the image of P have the same distance.
"""

import fitz

# Source code of fitz.util_hor_matrix:
def util_hor_matrix(C, P):
    '''
    Return the matrix that maps two points C, P to the x-axis such that
    C -> (0,0) and the image of P have the same distance.
    '''
    c = JM_point_from_py(C)
    p = JM_point_from_py(P)
    
    # compute (cosine, sine) of vector P-C with double precision:
    s = mupdf.fz_normalize_vector(mupdf.fz_make_point(p.x - c.x, p.y - c.y))
    
    m1 = mupdf.fz_make_matrix(1, 0, 0, 1, -c.x, -c.y)
    m2 = mupdf.fz_make_matrix(s.x, -s.y, s.y, s.x, 0, 0)
    return JM_py_from_matrix(mupdf.fz_concat(m1, m2))
