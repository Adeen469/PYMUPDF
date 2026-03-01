"""
Function: fitz.JM_rects_overlap
Signature: JM_rects_overlap(a, b)
Description: No docstring available.
"""

import fitz

# Source code of fitz.JM_rects_overlap:
def JM_rects_overlap(a, b):
    if (0
            or a.x0 >= b.x1
            or a.y0 >= b.y1
            or a.x1 <= b.x0
            or a.y1 <= b.y0
            ):
        return 0
    return 1
