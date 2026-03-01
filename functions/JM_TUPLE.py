"""
Function: fitz.JM_TUPLE
Signature: JM_TUPLE(o: Sequence) -> tuple
Description: No docstring available.
"""

import fitz

# Source code of fitz.JM_TUPLE:
def JM_TUPLE(o: typing.Sequence) -> tuple:
    return tuple(map(lambda x: round(x, 5) if abs(x) >= 1e-4 else 0, o))
