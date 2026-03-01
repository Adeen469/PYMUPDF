"""
Function: fitz.JM_TUPLE3
Signature: JM_TUPLE3(o: Sequence) -> tuple
Description: No docstring available.
"""

import fitz

# Source code of fitz.JM_TUPLE3:
def JM_TUPLE3(o: typing.Sequence) -> tuple:
    return tuple(map(lambda x: round(x, 3) if abs(x) >= 1e-3 else 0, o))
