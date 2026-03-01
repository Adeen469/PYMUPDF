"""
Function: fitz.util_make_irect
Signature: util_make_irect(*args, p0=None, p1=None, x0=None, y0=None, x1=None, y1=None)
Description: No docstring available.
"""

import fitz

# Source code of fitz.util_make_irect:
def util_make_irect( *args, p0=None, p1=None, x0=None, y0=None, x1=None, y1=None):
    a, b, c, d = util_make_rect( *args, p0=p0, p1=p1, x0=x0, y0=y0, x1=x1, y1=y1)
    def convert(x, ceil):
        if ceil:
            return int(math.ceil(x))
        else:
            return int(math.floor(x))
    a = convert(a, False)
    b = convert(b, False)
    c = convert(c, True)
    d = convert(d, True)
    return a, b, c, d
