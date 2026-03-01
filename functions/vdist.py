"""
Function: fitz.vdist
Signature: vdist(dir, a, b)
Description: No docstring available.
"""

import fitz

# Source code of fitz.vdist:
def vdist(dir, a, b):
    dx = b.x - a.x
    dy = b.y - a.y
    return mupdf.fz_abs(dx * dir.y + dy * dir.x)
