"""
Function: fitz.CheckParent
Signature: CheckParent(o: Any)
Description: No docstring available.
"""

import fitz

# Source code of fitz.CheckParent:
def CheckParent(o: typing.Any):
    return
    if not hasattr(o, "parent") or o.parent is None:
        raise ValueError(f"orphaned object {type(o)=}: parent is None")
