"""
Function: fitz.PDF_NAME
Signature: PDF_NAME(x)
Description: No docstring available.
"""

import fitz

# Source code of fitz.PDF_NAME:
def PDF_NAME(x):
    assert isinstance(x, str)
    ret = getattr(mupdf, f'PDF_ENUM_NAME_{x}')
    # Note that we return a (swig proxy for) pdf_obj*, not a mupdf.PdfObj. In
    # the C++ API, the constructor PdfObj::PdfObj(pdf_obj*) is marked as
    # explicit, but this seems to be ignored by SWIG. If SWIG started to
    # generate code that respected `explicit`, we would need to do `return
    # mupdf.PdfObj(ret)`.
    #
    # [Compare with extra.i, where we define our own PDF_NAME2() macro that
    # returns a mupdf::PdfObj.]
    return ret
