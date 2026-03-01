"""
Function: fitz.colors_pdf_dict
Signature: colors_pdf_dict()
Description:
Returns dict mapping from name to (red, green, blue).
    name: lower-case name.
    red, green, blue: float in range 0..1.
"""

import fitz

# Source code of fitz.colors_pdf_dict:
def colors_pdf_dict():
    '''
    Returns dict mapping from name to (red, green, blue).
        name: lower-case name.
        red, green, blue: float in range 0..1.
    '''
    return pdfcolor
