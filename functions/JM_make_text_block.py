"""
Function: fitz.JM_make_text_block
Signature: JM_make_text_block(block, block_dict, raw, buff, tp_rect)
Description: No docstring available.
"""

import fitz

# Source code of fitz.JM_make_text_block:
def JM_make_text_block(block, block_dict, raw, buff, tp_rect):
    if 1 or g_use_extra:
        return extra.JM_make_text_block(block.m_internal, block_dict, raw, buff.m_internal, tp_rect.m_internal)
    line_list = []
    block_rect = mupdf.FzRect(mupdf.FzRect.Fixed_EMPTY)
    #log(f'{block=}')
    for line in block:
        #log(f'{line=}')
        if (mupdf.fz_is_empty_rect(mupdf.fz_intersect_rect(tp_rect, mupdf.FzRect(line.m_internal.bbox)))
                and not mupdf.fz_is_infinite_rect(tp_rect)
                ):
            continue
        line_dict = dict()
        line_rect = JM_make_spanlist(line_dict, line, raw, buff, tp_rect)
        block_rect = mupdf.fz_union_rect(block_rect, line_rect)
        line_dict[dictkey_wmode] = line.m_internal.wmode
        line_dict[dictkey_dir] = JM_py_from_point(line.m_internal.dir)
        line_dict[dictkey_bbox] = JM_py_from_rect(line_rect)
        line_list.append(line_dict)
    block_dict[dictkey_bbox] = JM_py_from_rect(block_rect)
    block_dict[dictkey_lines] = line_list
