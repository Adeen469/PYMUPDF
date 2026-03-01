"""
Function: fitz.JM_search_stext_page
Signature: JM_search_stext_page(page, needle)
Description: No docstring available.
"""

import fitz

# Source code of fitz.JM_search_stext_page:
def JM_search_stext_page(page, needle):
    if 1 or g_use_extra:
        return extra.JM_search_stext_page(page.m_internal, needle)
    
    rect = mupdf.FzRect(page.m_internal.mediabox)
    if not needle:
        return
    quads = []
    class Hits:
        def __str__(self):
            return f'Hits(len={self.len} quads={self.quads} hfuzz={self.hfuzz} vfuzz={self.vfuzz}'
    hits = Hits()
    hits.len = 0
    hits.quads = quads
    hits.hfuzz = 0.2    # merge kerns but not large gaps
    hits.vfuzz = 0.1

    buffer_ = JM_new_buffer_from_stext_page(page)
    haystack_string = mupdf.fz_string_from_buffer(buffer_)
    haystack = 0
    begin, end = find_string(haystack_string[haystack:], needle)
    if begin is None:
        #goto no_more_matches;
        return quads

    begin += haystack
    end += haystack
    inside = 0
    i = 0
    for block in page:
        if block.m_internal.type != mupdf.FZ_STEXT_BLOCK_TEXT:
            continue
        for line in block:
            for ch in line:
                i += 1
                if not mupdf.fz_is_infinite_rect(rect):
                    r = JM_char_bbox(line, ch)
                    if not JM_rects_overlap(rect, r):
                        #goto next_char;
                        continue
                while 1:
                    #try_new_match:
                    if not inside:
                        if haystack >= begin:
                            inside = 1
                    if inside:
                        if haystack < end:
                            on_highlight_char(hits, line, ch)
                            break
                        else:
                            inside = 0
                            begin, end = find_string(haystack_string[haystack:], needle)
                            if begin is None:
                                #goto no_more_matches;
                                return quads
                            else:
                                #goto try_new_match;
                                begin += haystack
                                end += haystack
                                continue
                    break
                haystack += 1
                #next_char:;
            assert haystack_string[haystack] == '\n', \
                    f'{haystack=} {haystack_string[haystack]=}'
            haystack += 1
        assert haystack_string[haystack] == '\n', \
                f'{haystack=} {haystack_string[haystack]=}'
        haystack += 1
    #no_more_matches:;
    return quads
