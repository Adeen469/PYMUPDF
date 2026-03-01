"""
Function: fitz.JM_UnicodeFromBuffer
Signature: JM_UnicodeFromBuffer(buff)
Description: No docstring available.
"""

import fitz

# Source code of fitz.JM_UnicodeFromBuffer:
def JM_UnicodeFromBuffer(buff):
    buff_bytes = mupdf.fz_buffer_extract_copy(buff)
    val = buff_bytes.decode(errors='replace')
    z = val.find(chr(0))
    if z >= 0:
        val = val[:z]
    return val
