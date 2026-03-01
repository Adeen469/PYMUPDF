"""
Function: fitz.JM_EscapeStrFromBuffer
Signature: JM_EscapeStrFromBuffer(buff)
Description: No docstring available.
"""

import fitz

# Source code of fitz.JM_EscapeStrFromBuffer:
def JM_EscapeStrFromBuffer(buff):
    if not buff.m_internal:
        return ''
    s = mupdf.fz_buffer_extract_copy(buff)
    val = PyUnicode_DecodeRawUnicodeEscape(s, errors='replace')
    return val
