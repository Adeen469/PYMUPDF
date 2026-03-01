"""
Function: fitz.PyUnicode_DecodeRawUnicodeEscape
Signature: PyUnicode_DecodeRawUnicodeEscape(s, errors='strict')
Description: No docstring available.
"""

import fitz

# Source code of fitz.PyUnicode_DecodeRawUnicodeEscape:
def PyUnicode_DecodeRawUnicodeEscape(s, errors='strict'):
    # FIXED: handle raw unicode escape sequences
    if not s:
        return ""
    if isinstance(s, str):
        rc = s.encode("utf8", errors=errors)
    elif isinstance(s, bytes):
        rc = s[:]
    ret = rc.decode('raw_unicode_escape', errors=errors)
    return ret
