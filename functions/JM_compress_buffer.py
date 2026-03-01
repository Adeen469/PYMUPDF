"""
Function: fitz.JM_compress_buffer
Signature: JM_compress_buffer(inbuffer)
Description:
compress char* into a new buffer
"""

import fitz

# Source code of fitz.JM_compress_buffer:
def JM_compress_buffer(inbuffer):
    '''
    compress char* into a new buffer
    '''
    data, compressed_length = mupdf.fz_new_deflated_data_from_buffer(
            inbuffer,
            mupdf.FZ_DEFLATE_BEST,
            )
    #log( '{=data compressed_length}')
    if not data or compressed_length == 0:
        return None
    buf = mupdf.FzBuffer(mupdf.fz_new_buffer_from_data(data, compressed_length))
    mupdf.fz_resize_buffer(buf, compressed_length)
    return buf
