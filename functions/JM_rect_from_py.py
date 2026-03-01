"""
Function: fitz.JM_rect_from_py
Signature: JM_rect_from_py(r)
Description: No docstring available.
"""

import fitz

# Source code of fitz.JM_rect_from_py:
def JM_rect_from_py(r):
    if isinstance(r, mupdf.FzRect):
        return r
    if isinstance(r, mupdf.FzIrect):
        return mupdf.FzRect(r)
    if isinstance(r, Rect):
        return mupdf.fz_make_rect(r.x0, r.y0, r.x1, r.y1)
    if isinstance(r, IRect):
        return mupdf.fz_make_rect(r.x0, r.y0, r.x1, r.y1)
    if not r or not PySequence_Check(r) or PySequence_Size(r) != 4:
        return mupdf.FzRect(mupdf.FzRect.Fixed_INFINITE)
    f = [0, 0, 0, 0]
    for i in range(4):
        f[i] = JM_FLOAT_ITEM(r, i)
        if f[i] is None:
            return mupdf.FzRect(mupdf.FzRect.Fixed_INFINITE)
        if f[i] < FZ_MIN_INF_RECT:
            f[i] = FZ_MIN_INF_RECT
        if f[i] > FZ_MAX_INF_RECT:
            f[i] = FZ_MAX_INF_RECT
    return mupdf.fz_make_rect(f[0], f[1], f[2], f[3])
