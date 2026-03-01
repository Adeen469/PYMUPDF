"""
Function: fitz.CheckMarkerArg
Signature: CheckMarkerArg(quads: Any) -> tuple
Description: No docstring available.
"""

import fitz

# Source code of fitz.CheckMarkerArg:
def CheckMarkerArg(quads: typing.Any) -> tuple:
    if CheckRect(quads):
        r = Rect(quads)
        return (r.quad,)
    if CheckQuad(quads):
        return (quads,)
    for q in quads:
        if not (CheckRect(q) or CheckQuad(q)):
            raise ValueError("bad quads entry")
    return quads
