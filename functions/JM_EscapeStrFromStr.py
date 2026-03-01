"""
Function: fitz.JM_EscapeStrFromStr
Signature: JM_EscapeStrFromStr(c)
Description: No docstring available.
"""

import fitz

# Source code of fitz.JM_EscapeStrFromStr:
def JM_EscapeStrFromStr(c):
    # `c` is typically from SWIG which will have converted a `const char*` from
    # C into a Python `str` using `PyUnicode_DecodeUTF8(carray, static_cast<
    # Py_ssize_t >(size), "surrogateescape")`.  This gives us a Python `str`
    # with some characters encoded as a \0xdcXY sequence, where `XY` are hex
    # digits for an invalid byte in the original `const char*`.
    #
    # This is actually a reasonable way of representing arbitrary
    # strings from C, but we want to mimic what PyMuPDF does. It uses
    # `PyUnicode_DecodeRawUnicodeEscape(c, (Py_ssize_t) strlen(c), "replace")`
    # which gives a string containing actual unicode characters for any invalid
    # bytes.
    #
    # We mimic this by converting the `str` to a `bytes` with 'surrogateescape'
    # to recognise \0xdcXY sequences, then convert the individual bytes into a
    # `str` using `chr()`.
    #
    # Would be good to have a more efficient way to do this.
    #
    if c is None:
        return ''
    assert isinstance(c, str), f'{type(c)=}'
    b = c.encode('utf8', 'surrogateescape')
    ret = ''
    for bb in b:
        ret += chr(bb)
    return ret
