"""
Function: fitz.JM_BufferFromBytes
Signature: JM_BufferFromBytes(stream)
Description:
Make fz_buffer from a PyBytes, PyByteArray or io.BytesIO object. If a text
io.BytesIO, we convert to binary by encoding as utf8.
"""

import fitz

# Source code of fitz.JM_BufferFromBytes:
def JM_BufferFromBytes(stream):
    '''
    Make fz_buffer from a PyBytes, PyByteArray or io.BytesIO object. If a text
    io.BytesIO, we convert to binary by encoding as utf8.
    '''
    if isinstance(stream, (bytes, bytearray)):
        data = stream
    elif hasattr(stream, 'getvalue'):
        data = stream.getvalue()
        if isinstance(data, str):
            data = data.encode('utf-8')
        if not isinstance(data, (bytes, bytearray)):
            raise Exception(f'.getvalue() returned unexpected type: {type(data)}')
    else:
        return mupdf.FzBuffer()
    return mupdf.fz_new_buffer_from_copied_data(data)
