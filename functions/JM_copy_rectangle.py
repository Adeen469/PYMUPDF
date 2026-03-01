"""
Function: fitz.JM_copy_rectangle
Signature: JM_copy_rectangle(page, area)
Description: No docstring available.
"""

import fitz

# Source code of fitz.JM_copy_rectangle:
def JM_copy_rectangle(page, area):
    need_new_line = 0
    buffer = io.StringIO()
    for block in page:
        if block.m_internal.type != mupdf.FZ_STEXT_BLOCK_TEXT:
            continue
        for line in block:
            line_had_text = 0
            for ch in line:
                r = JM_char_bbox(line, ch)
                if JM_rects_overlap(area, r):
                    line_had_text = 1
                    if need_new_line:
                        buffer.write("\n")
                        need_new_line = 0
                    buffer.write(make_escape(ch.m_internal.c))
            if line_had_text:
                need_new_line = 1

    s = buffer.getvalue()   # take over the data
    return s
