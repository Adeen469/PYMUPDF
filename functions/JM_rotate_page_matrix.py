"""
Function: fitz.JM_rotate_page_matrix
Signature: JM_rotate_page_matrix(page)
Description:
calculate page rotation matrices
"""

import fitz

# Source code of fitz.JM_rotate_page_matrix:
def JM_rotate_page_matrix(page):
    '''
    calculate page rotation matrices
    '''
    if not page.m_internal:
        return mupdf.FzMatrix()  # no valid pdf page given
    rotation = JM_page_rotation(page)
    #log( '{rotation=}')
    if rotation == 0:
        return mupdf.FzMatrix()  # no rotation
    cb_size = JM_cropbox_size(page.obj())
    w = cb_size.x
    h = cb_size.y
    #log( '{=h w}')
    if rotation == 90:
        m = mupdf.fz_make_matrix(0, 1, -1, 0, h, 0)
    elif rotation == 180:
        m = mupdf.fz_make_matrix(-1, 0, 0, -1, w, h)
    else:
        m = mupdf.fz_make_matrix(0, -1, 1, 0, 0, w)
    #log( 'returning {m=}')
    return m
