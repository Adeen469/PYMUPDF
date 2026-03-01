"""
Function: fitz.ColorCode
Signature: ColorCode(c: Union[list, tuple, float, NoneType], f: str) -> str
Description: No docstring available.
"""

import fitz

# Source code of fitz.ColorCode:
def ColorCode(c: typing.Union[list, tuple, float, None], f: str) -> str:
    if not c:
        return ""
    if hasattr(c, "__float__"):
        c = (c,)
    CheckColor(c)
    if len(c) == 1:
        s = _format_g(c[0]) + " "
        return s + "G " if f == "c" else s + "g "

    if len(c) == 3:
        s = _format_g(tuple(c)) + " "
        return s + "RG " if f == "c" else s + "rg "

    s = _format_g(tuple(c)) + " "
    return s + "K " if f == "c" else s + "k "
