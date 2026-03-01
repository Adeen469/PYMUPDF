"""
Function: fitz.JM_color_count
Signature: JM_color_count(pm, clip)
Description: No docstring available.
"""

import fitz

# Source code of fitz.JM_color_count:
def JM_color_count( pm, clip):
    if 1 or g_use_extra:
        return extra.ll_JM_color_count(pm.m_internal, clip)
    
    rc = dict()
    cnt = 0
    irect = mupdf.fz_pixmap_bbox( pm)
    irect = mupdf.fz_intersect_irect(irect, mupdf.fz_round_rect(JM_rect_from_py(clip)))
    stride = pm.stride()
    width = irect.x1 - irect.x0
    height = irect.y1 - irect.y0
    n = pm.n()
    substride = width * n
    s = stride * (irect.y0 - pm.y()) + (irect.x0 - pm.x()) * n
    oldpix = _read_samples( pm, s, n)
    cnt = 0
    if mupdf.fz_is_empty_irect(irect):
        return rc
    for i in range( height):
        for j in range( 0, substride, n):
            newpix = _read_samples( pm, s + j, n)
            if newpix != oldpix:
                pixel = oldpix
                c = rc.get( pixel, None)
                if c is not None:
                    cnt += c
                rc[ pixel] = cnt
                cnt = 1
                oldpix = newpix
            else:
                cnt += 1
        s += stride
    pixel = oldpix
    c = rc.get( pixel)
    if c is not None:
        cnt += c
    rc[ pixel] = cnt
    return rc
