"""
Function: fitz.JM_derotate_page_matrix
Signature: JM_derotate_page_matrix(page)
Description:
just the inverse of rotation
"""

import fitz

# Source code of fitz.JM_derotate_page_matrix:
def JM_derotate_page_matrix(page):
    '''
    just the inverse of rotation
    '''
    mp = JM_rotate_page_matrix(page)
    return mupdf.fz_invert_matrix(mp)
