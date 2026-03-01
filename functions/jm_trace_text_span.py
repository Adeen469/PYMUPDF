"""
Function: fitz.jm_trace_text_span
Signature: jm_trace_text_span(dev, span, type_, ctm, colorspace, color, alpha, seqno)
Description:
jm_trace_text_span(fz_context *ctx, PyObject *out, fz_text_span *span, int type, fz_matrix ctm, fz_colorspace *colorspace, const float *color, float alpha, size_t seqno)
"""

import fitz

# Source code of fitz.jm_trace_text_span:
def jm_trace_text_span(dev, span, type_, ctm, colorspace, color, alpha, seqno):
    '''
    jm_trace_text_span(fz_context *ctx, PyObject *out, fz_text_span *span, int type, fz_matrix ctm, fz_colorspace *colorspace, const float *color, float alpha, size_t seqno)
    '''
    out_font = None
    assert isinstance( span, mupdf.fz_text_span)
    span = mupdf.FzTextSpan( span)
    assert isinstance( ctm, mupdf.fz_matrix)
    ctm = mupdf.FzMatrix( ctm)
    fontname = JM_font_name( span.font())
    #float rgb[3];
    #PyObject *chars = PyTuple_New(span->len);
    
    mat = mupdf.fz_concat(span.trm(), ctm)  # text transformation matrix
    dir = mupdf.fz_transform_vector(mupdf.fz_make_point(1, 0), mat) # writing direction
    fsize = math.sqrt(dir.x * dir.x + dir.y * dir.y)  # font size

    dir = mupdf.fz_normalize_vector(dir)

    space_adv = 0
    asc = JM_font_ascender( span.font())
    dsc = JM_font_descender( span.font())
    if asc < 1e-3:  # probably Tesseract font
        dsc = -0.1
        asc = 0.9

    # compute effective ascender / descender
    ascsize = asc * fsize / (asc - dsc)
    dscsize = dsc * fsize / (asc - dsc)
    fflags = 0  # font flags
    mono = mupdf.fz_font_is_monospaced( span.font())
    fflags += mono * TEXT_FONT_MONOSPACED
    fflags += mupdf.fz_font_is_italic( span.font()) * TEXT_FONT_ITALIC
    fflags += mupdf.fz_font_is_serif( span.font()) * TEXT_FONT_SERIFED
    fflags += mupdf.fz_font_is_bold( span.font()) * TEXT_FONT_BOLD

    last_adv = 0

    # walk through characters of span
    span_bbox = mupdf.FzRect()
    rot = mupdf.fz_make_matrix(dir.x, dir.y, -dir.y, dir.x, 0, 0)
    if dir.x == -1: # left-right flip
        rot.d = 1

    chars = []
    for i in range( span.m_internal.len):
        adv = 0
        if span.items(i).gid >= 0:
            adv = mupdf.fz_advance_glyph( span.font(), span.items(i).gid, span.m_internal.wmode)
        adv *= fsize
        last_adv = adv
        if span.items(i).ucs == 32:
            space_adv = adv
        char_orig = mupdf.fz_make_point(span.items(i).x, span.items(i).y)
        char_orig = mupdf.fz_transform_point(char_orig, ctm)
        m1 = mupdf.fz_make_matrix(1, 0, 0, 1, -char_orig.x, -char_orig.y)
        m1 = mupdf.fz_concat(m1, rot)
        m1 = mupdf.fz_concat(m1, mupdf.FzMatrix(1, 0, 0, 1, char_orig.x, char_orig.y))
        x0 = char_orig.x
        x1 = x0 + adv
        if (
                (mat.d > 0 and (dir.x == 1 or dir.x == -1))
                or
                (mat.b != 0 and mat.b == -mat.c)
                ):  # up-down flip
            y0 = char_orig.y + dscsize
            y1 = char_orig.y + ascsize
        else:
            y0 = char_orig.y - ascsize
            y1 = char_orig.y - dscsize
        char_bbox = mupdf.fz_make_rect(x0, y0, x1, y1)
        char_bbox = mupdf.fz_transform_rect(char_bbox, m1)
        chars.append(
                (
                    span.items(i).ucs,
                    span.items(i).gid,
                    (
                        char_orig.x,
                        char_orig.y,
                    ),
                    (
                        char_bbox.x0,
                        char_bbox.y0,
                        char_bbox.x1,
                        char_bbox.y1,
                    ),
                )
                )
        if i > 0:
            span_bbox = mupdf.fz_union_rect(span_bbox, char_bbox)
        else:
            span_bbox = char_bbox
    chars = tuple(chars)
    
    if not space_adv:
        if not (fflags & TEXT_FONT_MONOSPACED):
            c, out_font = mupdf.fz_encode_character_with_fallback( span.font(), 32, 0, 0)
            space_adv = mupdf.fz_advance_glyph(
                    span.font(),
                    c,
                    span.m_internal.wmode,
                    )
            space_adv *= fsize
            if not space_adv:
                space_adv = last_adv
        else:
            space_adv = last_adv    # for mono, any char width suffices

    # make the span dictionary
    span_dict = dict()
    span_dict[ 'dir'] = JM_py_from_point(dir)
    span_dict[ 'font'] = JM_EscapeStrFromStr(fontname)
    span_dict[ 'wmode'] = span.m_internal.wmode
    span_dict[ 'flags'] =fflags
    span_dict[ "bidi_lvl"] =span.m_internal.bidi_level
    span_dict[ "bidi_dir"] = span.m_internal.markup_dir
    span_dict[ 'ascender'] = asc
    span_dict[ 'descender'] = dsc
    span_dict[ 'colorspace'] = 3
    
    if colorspace:
        rgb = mupdf.fz_convert_color(
                mupdf.FzColorspace( mupdf.ll_fz_keep_colorspace( colorspace)),
                color,
                mupdf.fz_device_rgb(),
                mupdf.FzColorspace(),
                mupdf.FzColorParams(),
                )
        rgb = rgb[:3]   # mupdf.fz_convert_color() always returns 4 items.
    else:
        rgb = (0, 0, 0)
    
    if dev.linewidth > 0:   # width of character border
        linewidth = dev.linewidth
    else:
        linewidth = fsize * 0.05    # default: 5% of font size
    #log(f'{dev.linewidth=:.4f} {fsize=:.4f} {linewidth=:.4f}')
    
    span_dict[ 'color'] = rgb
    span_dict[ 'size'] = fsize
    span_dict[ "opacity"] = alpha
    span_dict[ "linewidth"] = linewidth
    span_dict[ "spacewidth"] = space_adv
    span_dict[ 'type'] = type_
    span_dict[ 'bbox'] = JM_py_from_rect(span_bbox)
    span_dict[ 'layer'] = dev.layer_name
    span_dict[ "seqno"] = seqno
    span_dict[ 'chars'] = chars
    #log(f'{span_dict=}')
    dev.out.append( span_dict)
