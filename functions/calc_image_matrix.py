"""
Function: fitz.calc_image_matrix
Signature: calc_image_matrix(width, height, tr, rotate, keep)
Description:
# compute image insertion matrix
"""

import fitz

# Source code of fitz.calc_image_matrix:
def calc_image_matrix(width, height, tr, rotate, keep):
    '''
    # compute image insertion matrix
    '''
    trect = JM_rect_from_py(tr)
    rot = mupdf.fz_rotate(rotate)
    trw = trect.x1 - trect.x0
    trh = trect.y1 - trect.y0
    w = trw
    h = trh
    if keep:
        large = max(width, height)
        fw = width / large
        fh = height / large
    else:
        fw = fh = 1
    small = min(fw, fh)
    if rotate != 0 and rotate != 180:
        f = fw
        fw = fh
        fh = f
    if fw < 1:
        if trw / fw > trh / fh:
            w = trh * small
            h = trh
        else:
            w = trw
            h = trw / small
    elif fw != fh:
        if trw / fw > trh / fh:
            w = trh / small
            h = trh
        else:
            w = trw
            h = trw * small
    else:
        w = trw
        h = trh
    tmp = mupdf.fz_make_point(
            (trect.x0 + trect.x1) / 2,
            (trect.y0 + trect.y1) / 2,
            )
    mat = mupdf.fz_make_matrix(1, 0, 0, 1, -0.5, -0.5)
    mat = mupdf.fz_concat(mat, rot)
    mat = mupdf.fz_concat(mat, mupdf.fz_scale(w, h))
    mat = mupdf.fz_concat(mat, mupdf.fz_translate(tmp.x, tmp.y))
    return mat
