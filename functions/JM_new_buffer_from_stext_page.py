"""
Function: fitz.JM_new_buffer_from_stext_page
Signature: JM_new_buffer_from_stext_page(page)
Description:
make a buffer from an stext_page's text
"""

import fitz

# Source code of fitz.JM_new_buffer_from_stext_page:
def JM_new_buffer_from_stext_page(page):
    '''
    make a buffer from an stext_page's text
    '''
    assert isinstance(page, mupdf.FzStextPage)
    rect = mupdf.FzRect(page.m_internal.mediabox)
    buf = mupdf.fz_new_buffer(256)
    for block in page:
        if block.m_internal.type == mupdf.FZ_STEXT_BLOCK_TEXT:
            for line in block:
                for ch in line:
                    if (not JM_rects_overlap(rect, JM_char_bbox(line, ch))
                            and not mupdf.fz_is_infinite_rect(rect)
                            ):
                        continue
                    mupdf.fz_append_rune(buf, ch.m_internal.c)
                mupdf.fz_append_byte(buf, ord('\n'))
            mupdf.fz_append_byte(buf, ord('\n'))
    return buf
