"""
Function: fitz.JM_pdf_obj_from_str
Signature: JM_pdf_obj_from_str(doc, src)
Description:
create PDF object from given string (new in v1.14.0: MuPDF dropped it)
"""

import fitz

# Source code of fitz.JM_pdf_obj_from_str:
def JM_pdf_obj_from_str(doc, src):
    '''
    create PDF object from given string (new in v1.14.0: MuPDF dropped it)
    '''
    # fixme: seems inefficient to convert to bytes instance then make another
    # copy inside fz_new_buffer_from_copied_data(), but no other way?
    #
    buffer_ = mupdf.fz_new_buffer_from_copied_data(bytes(src, 'utf8'))
    stream = mupdf.fz_open_buffer(buffer_)
    lexbuf = mupdf.PdfLexbuf(mupdf.PDF_LEXBUF_SMALL)
    result = mupdf.pdf_parse_stm_obj(doc, stream, lexbuf)
    return result
