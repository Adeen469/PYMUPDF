"""
Function: fitz.JM_have_operation
Signature: JM_have_operation(pdf)
Description:
Ensure valid journalling state
"""

import fitz

# Source code of fitz.JM_have_operation:
def JM_have_operation(pdf):
    '''
    Ensure valid journalling state
    '''
    if pdf.m_internal.journal and not mupdf.pdf_undoredo_step(pdf, 0):
        return 0
    return 1
