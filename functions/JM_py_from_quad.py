"""
Function: fitz.JM_py_from_quad
Signature: JM_py_from_quad(q)
Description:
PySequence from fz_quad.
"""

import fitz

# Source code of fitz.JM_py_from_quad:
def JM_py_from_quad(q):
    '''
    PySequence from fz_quad.
    '''
    return (
            (q.ul.x, q.ul.y),
            (q.ur.x, q.ur.y),
            (q.ll.x, q.ll.y),
            (q.lr.x, q.lr.y),
            )
