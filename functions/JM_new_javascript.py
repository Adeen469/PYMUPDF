"""
Function: fitz.JM_new_javascript
Signature: JM_new_javascript(pdf, value)
Description:
make new PDF action object from JavaScript source
Parameters are a PDF document and a Python string.
Returns a PDF action object.
"""

import fitz

# Source code of fitz.JM_new_javascript:
def JM_new_javascript(pdf, value):
    '''
    make new PDF action object from JavaScript source
    Parameters are a PDF document and a Python string.
    Returns a PDF action object.
    '''
    if value is None:
        # no argument given
        return
    data = JM_StrAsChar(value)
    if data is None:
        # not convertible to char*
        return

    res = mupdf.fz_new_buffer_from_copied_data(data.encode('utf8'))
    source = mupdf.pdf_add_stream(pdf, res, mupdf.PdfObj(), 0)
    newaction = mupdf.pdf_add_new_dict(pdf, 4)
    mupdf.pdf_dict_put(newaction, PDF_NAME('S'), mupdf.pdf_new_name('JavaScript'))
    mupdf.pdf_dict_put(newaction, PDF_NAME('JS'), source)
    return newaction
