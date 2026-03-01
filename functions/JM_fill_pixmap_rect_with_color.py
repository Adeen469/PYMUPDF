"""
Function: fitz.JM_fill_pixmap_rect_with_color
Signature: JM_fill_pixmap_rect_with_color(dest, col, b)
Description: No docstring available.
"""

import fitz

# Source code of fitz.JM_fill_pixmap_rect_with_color:
def JM_fill_pixmap_rect_with_color(dest, col, b):
    assert isinstance(dest, mupdf.FzPixmap)
    # fill a rect with a color tuple
    b = mupdf.fz_intersect_irect(b, mupdf.fz_pixmap_bbox( dest))
    w = b.x1 - b.x0
    y = b.y1 - b.y0
    if w <= 0 or y <= 0:
        return 0
    destspan = dest.stride()
    destp = destspan * (b.y0 - dest.y()) + dest.n() * (b.x0 - dest.x())
    while 1:
        s = destp
        for x in range(w):
            for i in range( dest.n()):
                mupdf.fz_samples_set(dest, s, col[i])
                s += 1
        destp += destspan
        y -= 1
        if y == 0:
            break
    return 1
