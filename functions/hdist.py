"""
Function: fitz.hdist
Signature: hdist(dir, a, b)
Description: No docstring available.
"""

import fitz

# Source code of fitz.hdist:
def hdist(dir, a, b):
    dx = b.x - a.x
    dy = b.y - a.y
    return mupdf.fz_abs(dx * dir.x + dy * dir.y)
