"""
Function: fitz.JM_StrAsChar
Signature: JM_StrAsChar(x)
Description: No docstring available.
"""

import fitz

# Source code of fitz.JM_StrAsChar:
def JM_StrAsChar(x):
    # fixme: should encode, but swig doesn't pass bytes to C as const char*.
    return x
    #return x.encode('utf8')
