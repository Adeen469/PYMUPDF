"""
Function: fitz.CheckMorph
Signature: CheckMorph(o: Any) -> bool
Description: No docstring available.
"""

import fitz

# Source code of fitz.CheckMorph:
def CheckMorph(o: typing.Any) -> bool:
    if not bool(o):
        return False
    if not (type(o) in (list, tuple) and len(o) == 2):
        raise ValueError("morph must be a sequence of length 2")
    if not (len(o[0]) == 2 and len(o[1]) == 6):
        raise ValueError("invalid morph param 0")
    if not o[1][4] == o[1][5] == 0:
        raise ValueError("invalid morph param 1")
    return True
