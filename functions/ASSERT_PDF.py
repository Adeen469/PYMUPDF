"""
Function: fitz.ASSERT_PDF
Signature: ASSERT_PDF(cond)
Description: No docstring available.
"""

import fitz

# Source code of fitz.ASSERT_PDF:
def ASSERT_PDF(cond):
    assert isinstance(cond, (mupdf.PdfPage, mupdf.PdfDocument)), f'{type(cond)=} {cond=}'
    if not cond.m_internal:
        raise Exception(MSG_IS_NO_PDF)
