"""
Function: fitz.JM_mupdf_warning
Signature: JM_mupdf_warning(text)
Description:
redirect MuPDF warnings
"""

import fitz

# Source code of fitz.JM_mupdf_warning:
def JM_mupdf_warning( text):
    '''
    redirect MuPDF warnings
    '''
    JM_mupdf_warnings_store.append(text)
    if JM_mupdf_show_warnings:
        message(f'MuPDF warning: {text}')
