"""
Function: fitz.CheckColor
Signature: CheckColor(c: Optional[Sequence])
Description: No docstring available.
"""

import fitz

# Source code of fitz.CheckColor:
def CheckColor(c: OptSeq):
    if c:
        if (
            type(c) not in (list, tuple)
            or len(c) not in (1, 3, 4)
            or min(c) < 0
            or max(c) > 1
        ):
            raise ValueError("need 1, 3 or 4 color components in range 0 to 1")
