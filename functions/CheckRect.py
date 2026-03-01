"""
Function: fitz.CheckRect
Signature: CheckRect(r: Any) -> bool
Description:
Check whether an object is non-degenerate rect-like.

It must be a sequence of 4 numbers.
"""

import fitz

# Source code of fitz.CheckRect:
def CheckRect(r: typing.Any) -> bool:
    """Check whether an object is non-degenerate rect-like.

    It must be a sequence of 4 numbers.
    """
    try:
        r = Rect(r)
    except Exception:
        if g_exceptions_verbose > 1:    exception_info()
        return False
    return not (r.is_empty or r.is_infinite)
