"""
Function: fitz.JM_update_stream
Signature: JM_update_stream(doc, obj, buffer_, compress)
Description:
update a stream object
compress stream when beneficial
"""

import fitz

# Source code of fitz.JM_update_stream:
def JM_update_stream(doc, obj, buffer_, compress):
    '''
    update a stream object
    compress stream when beneficial
    '''
    if compress:
        length, _ = mupdf.fz_buffer_storage(buffer_)
        if length > 30:   # ignore small stuff
            buffer_compressed = JM_compress_buffer(buffer_)
            assert isinstance(buffer_compressed, mupdf.FzBuffer)
            if buffer_compressed.m_internal:
                length_compressed, _ = mupdf.fz_buffer_storage(buffer_compressed)
                if length_compressed < length:  # was it worth the effort?
                    mupdf.pdf_dict_put(
                            obj,
                            mupdf.PDF_ENUM_NAME_Filter,
                            mupdf.PDF_ENUM_NAME_FlateDecode,
                            )
                    mupdf.pdf_update_stream(doc, obj, buffer_compressed, 1)
                    return
    
    mupdf.pdf_update_stream(doc, obj, buffer_, 0)
