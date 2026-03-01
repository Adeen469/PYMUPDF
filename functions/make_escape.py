"""
Function: fitz.make_escape
Signature: make_escape(ch)
Description: No docstring available.
"""

import fitz

# Source code of fitz.make_escape:
def make_escape(ch):
    if ch == 92:
        return "\\u005c"
    elif 32 <= ch <= 127 or ch == 10:
        return chr(ch)
    elif 0xd800 <= ch <= 0xdfff:  # orphaned surrogate
        return "\\ufffd"
    elif ch <= 0xffff:
        return "\\u%04x" % ch
    else:
        return "\\U%08x" % ch
