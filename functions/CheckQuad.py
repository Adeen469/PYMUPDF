"""
Function: fitz.CheckQuad
Signature: CheckQuad(q: Any) -> bool
Description:
Check whether an object is convex, not empty  quad-like.

It must be a sequence of 4 number pairs.
"""

import fitz

# Source code of fitz.CheckQuad:
def CheckQuad(q: typing.Any) -> bool:
    """Check whether an object is convex, not empty  quad-like.

    It must be a sequence of 4 number pairs.
    """
    try:
        q0 = Quad(q)
    except Exception:
        if g_exceptions_verbose > 1:    exception_info()
        return False
    return q0.is_convex
