"""
Function: fitz.JM_object_to_buffer
Signature: JM_object_to_buffer(what, compress, ascii)
Description: No docstring available.
"""

import fitz

# Source code of fitz.JM_object_to_buffer:
def JM_object_to_buffer(what, compress, ascii):
    res = mupdf.fz_new_buffer(512)
    out = mupdf.FzOutput(res)
    mupdf.pdf_print_obj(out, what, compress, ascii)
    out.fz_close_output()
    mupdf.fz_terminate_buffer(res)
    return res
