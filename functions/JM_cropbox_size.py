"""
Function: fitz.JM_cropbox_size
Signature: JM_cropbox_size(page_obj)
Description: No docstring available.
"""

import fitz

# Source code of fitz.JM_cropbox_size:
def JM_cropbox_size(page_obj):
    rect = JM_cropbox(page_obj)
    w = abs(rect.x1 - rect.x0)
    h = abs(rect.y1 - rect.y0)
    size = mupdf.fz_make_point(w, h)
    return size
