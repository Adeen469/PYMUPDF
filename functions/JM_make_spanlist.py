"""
Function: fitz.JM_make_spanlist
Signature: JM_make_spanlist(line_dict, line, raw, buff, tp_rect)
Description: No docstring available.
"""

import fitz

# Source code of fitz.JM_make_spanlist:
def JM_make_spanlist(line_dict, line, raw, buff, tp_rect):
    if 1 or g_use_extra:
        return extra.JM_make_spanlist(line_dict, line, raw, buff, tp_rect)
    char_list = None
    span_list = []
    mupdf.fz_clear_buffer(buff)
    span_rect = mupdf.FzRect(mupdf.FzRect.Fixed_EMPTY)
    line_rect = mupdf.FzRect(mupdf.FzRect.Fixed_EMPTY)

    class char_style:
        def __init__(self, rhs=None):
            if rhs:
                self.size = rhs.size
                self.flags = rhs.flags
                self.char_flags = rhs.char_flags
                self.font = rhs.font
                self.argb = rhs.argb
                self.asc = rhs.asc
                self.desc = rhs.desc
                self.bidi = rhs.bidi
            else:
                self.size = -1
                self.flags = -1
                self.char_flags = -1
                self.font = ''
                self.argb = -1
                self.asc = 0
                self.desc = 0
                self.bidi = 0
        def __str__(self):
            ret = f'{self.size} {self.flags}'
            ret += f' {self.char_flags}'
            ret += f' {self.font} {self.color} {self.asc} {self.desc}'
            return ret

    old_style = char_style()
    style = char_style()
    span = None
    span_origin = None

    for ch in line:
        # start-trace
        r = JM_char_bbox(line, ch)
        if (not JM_rects_overlap(tp_rect, r)
                and not mupdf.fz_is_infinite_rect(tp_rect)
                ):
            continue

        # Info from:
        # detect_super_script()
        # fz_font_is_italic()
        # fz_font_is_serif()
        # fz_font_is_monospaced()
        # fz_font_is_bold()
        
        flags = JM_char_font_flags(mupdf.FzFont(mupdf.ll_fz_keep_font(ch.m_internal.font)), line, ch)
        origin = mupdf.FzPoint(ch.m_internal.origin)
        style.size = ch.m_internal.size
        style.flags = flags
        # FZ_STEXT_SYNTHETIC is per-char, not per-span.
        style.char_flags = ch.m_internal.flags & ~mupdf.FZ_STEXT_SYNTHETIC
        style.font = JM_font_name(mupdf.FzFont(mupdf.ll_fz_keep_font(ch.m_internal.font)))
        style.argb = ch.m_internal.argb
        style.asc = JM_font_ascender(mupdf.FzFont(mupdf.ll_fz_keep_font(ch.m_internal.font)))
        style.desc = JM_font_descender(mupdf.FzFont(mupdf.ll_fz_keep_font(ch.m_internal.font)))
        style.bidi = ch.m_internal.bidi

        if (style.size != old_style.size
                or style.flags != old_style.flags
                or (style.char_flags != old_style.char_flags)
                or style.argb != old_style.argb
                or style.font != old_style.font
                or style.bidi != old_style.bidi
                ):
            if old_style.size >= 0:
                # not first one, output previous
                if raw:
                    # put character list in the span
                    span[dictkey_chars] = char_list
                    char_list = None
                else:
                    # put text string in the span
                    span[dictkey_text] = JM_EscapeStrFromBuffer( buff)
                    mupdf.fz_clear_buffer(buff)

                span[dictkey_origin] = JM_py_from_point(span_origin)
                span[dictkey_bbox] = JM_py_from_rect(span_rect)
                line_rect = mupdf.fz_union_rect(line_rect, span_rect)
                span_list.append( span)
                span = None

            span = dict()
            asc = style.asc
            desc = style.desc
            if style.asc < 1e-3:
                asc = 0.9
                desc = -0.1

            span[dictkey_size] = style.size
            span[dictkey_flags] = style.flags
            span[dictkey_bidi] = style.bidi
            span[dictkey_char_flags] = style.char_flags
            span[dictkey_font] = JM_EscapeStrFromStr(style.font)
            span[dictkey_color] = style.argb & 0xffffff
            span['alpha'] = style.argb >> 24
            span["ascender"] = asc
            span["descender"] = desc

            # Need to be careful here - doing 'old_style=style' does a shallow
            # copy, but we need to keep old_style as a distinct instance.
            old_style = char_style(style)
            span_rect = r
            span_origin = origin

        span_rect = mupdf.fz_union_rect(span_rect, r)

        if raw: # make and append a char dict
            char_dict = dict()
            char_dict[dictkey_origin] = JM_py_from_point( ch.m_internal.origin)
            char_dict[dictkey_bbox] = JM_py_from_rect(r)
            char_dict[dictkey_c] = chr(ch.m_internal.c)
            char_dict['synthetic'] = bool(ch.m_internal.flags & mupdf.FZ_STEXT_SYNTHETIC)

            if char_list is None:
                char_list = []
            char_list.append(char_dict)
        else:   # add character byte to buffer
            JM_append_rune(buff, ch.m_internal.c)

    # all characters processed, now flush remaining span
    if span:
        if raw:
            span[dictkey_chars] = char_list
            char_list = None
        else:
            span[dictkey_text] = JM_EscapeStrFromBuffer(buff)
            mupdf.fz_clear_buffer(buff)
        span[dictkey_origin] = JM_py_from_point(span_origin)
        span[dictkey_bbox] = JM_py_from_rect(span_rect)

        if not mupdf.fz_is_empty_rect(span_rect):
            span_list.append(span)
            line_rect = mupdf.fz_union_rect(line_rect, span_rect)
        span = None
    if not mupdf.fz_is_empty_rect(line_rect):
        line_dict[dictkey_spans] = span_list
    else:
        line_dict[dictkey_spans] = span_list
    return line_rect
