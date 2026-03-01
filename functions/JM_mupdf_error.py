"""
Function: fitz.JM_mupdf_error
Signature: JM_mupdf_error(text)
Description: No docstring available.
"""

import fitz

# Source code of fitz.JM_mupdf_error:
def JM_mupdf_error( text):
    JM_mupdf_warnings_store.append(text)
    if JM_mupdf_show_errors:
        message(f'MuPDF error: {text}\n')
