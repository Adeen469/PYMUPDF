"""
Function: fitz.JM_char_bbox
Signature: JM_char_bbox(line, ch)
Description:
return rect of char quad
"""

import fitz

# Source code of fitz.JM_char_bbox:
def JM_char_bbox(line, ch):
    '''
    return rect of char quad
    '''
    q = JM_char_quad(line, ch)
    r = mupdf.fz_rect_from_quad(q)
    if not line.m_internal.wmode:
        return r
    if r.y1 < r.y0 + ch.m_internal.size:
        r.y0 = r.y1 - ch.m_internal.size
    return r
