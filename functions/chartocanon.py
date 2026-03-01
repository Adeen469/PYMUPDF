"""
Function: fitz.chartocanon
Signature: chartocanon(s)
Description: No docstring available.
"""

import fitz

# Source code of fitz.chartocanon:
def chartocanon(s):
    assert isinstance(s, str)
    n, c = mupdf.fz_chartorune(s)
    c = canon(c)
    return n, c
