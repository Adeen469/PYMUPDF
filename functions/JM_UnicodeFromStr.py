"""
Function: fitz.JM_UnicodeFromStr
Signature: JM_UnicodeFromStr(s)
Description: No docstring available.
"""

import fitz

# Source code of fitz.JM_UnicodeFromStr:
def JM_UnicodeFromStr(s):
    if s is None:
        return ''
    if isinstance(s, bytes):
        s = s.decode('utf8')
    assert isinstance(s, str), f'{type(s)=} {s=}'
    return s
