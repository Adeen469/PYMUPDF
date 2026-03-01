"""
Function: fitz.JM_matrix_from_py
Signature: JM_matrix_from_py(m)
Description: No docstring available.
"""

import fitz

# Source code of fitz.JM_matrix_from_py:
def JM_matrix_from_py(m):
    a = [0, 0, 0, 0, 0, 0]
    if isinstance(m, mupdf.FzMatrix):
        return m
    if isinstance(m, Matrix):
        return mupdf.FzMatrix(m.a, m.b, m.c, m.d, m.e, m.f)
    if not m or not PySequence_Check(m) or PySequence_Size(m) != 6:
        return mupdf.FzMatrix()
    for i in range(6):
        a[i] = JM_FLOAT_ITEM(m, i)
        if a[i] is None:
            return mupdf.FzRect()
    return mupdf.FzMatrix(a[0], a[1], a[2], a[3], a[4], a[5])
