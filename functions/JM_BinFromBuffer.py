"""
Function: fitz.JM_BinFromBuffer
Signature: JM_BinFromBuffer(buffer_)
Description:
Turn fz_buffer into a Python bytes object
"""

import fitz

# Source code of fitz.JM_BinFromBuffer:
def JM_BinFromBuffer(buffer_):
    '''
    Turn fz_buffer into a Python bytes object
    '''
    assert isinstance(buffer_, mupdf.FzBuffer)
    ret = mupdf.fz_buffer_extract_copy(buffer_)
    return ret
