"""
Function: fitz.JM_char_quad
Signature: JM_char_quad(line, ch)
Description:
re-compute char quad if ascender/descender values make no sense
"""

import fitz

# Source code of fitz.JM_char_quad:
def JM_char_quad(line, ch):
    '''
    re-compute char quad if ascender/descender values make no sense
    '''
    if 1 and g_use_extra:
        # This reduces time taken to extract text from PyMuPDF.pdf from 20s to
        # 15s.
        return mupdf.FzQuad(extra.JM_char_quad( line.m_internal, ch.m_internal))
        
    assert isinstance(line, mupdf.FzStextLine)
    assert isinstance(ch, mupdf.FzStextChar)
    if _globals.skip_quad_corrections:   # no special handling
        return ch.quad
    if line.m_internal.wmode:  # never touch vertical write mode
        return ch.quad
    font = mupdf.FzFont(mupdf.ll_fz_keep_font(ch.m_internal.font))
    asc = JM_font_ascender(font)
    dsc = JM_font_descender(font)
    fsize = ch.m_internal.size
    asc_dsc = asc - dsc + FLT_EPSILON
    if asc_dsc >= 1 and _globals.small_glyph_heights == 0:   # no problem
        return mupdf.FzQuad(ch.m_internal.quad)

    # Re-compute quad with adjusted ascender / descender values:
    # Move ch->origin to (0,0) and de-rotate quad, then adjust the corners,
    # re-rotate and move back to ch->origin location.
    fsize = ch.m_internal.size
    bbox = mupdf.fz_font_bbox(font)
    fwidth = bbox.x1 - bbox.x0
    if asc < 1e-3:  # probably Tesseract glyphless font
        dsc = -0.1
        asc = 0.9
        asc_dsc = 1.0
    
    if _globals.small_glyph_heights or asc_dsc < 1:
        dsc = dsc / asc_dsc
        asc = asc / asc_dsc
    asc_dsc = asc - dsc
    asc = asc * fsize / asc_dsc
    dsc = dsc * fsize / asc_dsc
    
    # Re-compute quad with the adjusted ascender / descender values:
    # Move ch->origin to (0,0) and de-rotate quad, then adjust the corners,
    # re-rotate and move back to ch->origin location.
    c = line.m_internal.dir.x  # cosine
    s = line.m_internal.dir.y  # sine
    trm1 = mupdf.fz_make_matrix(c, -s, s, c, 0, 0) # derotate
    trm2 = mupdf.fz_make_matrix(c, s, -s, c, 0, 0) # rotate
    if (c == -1):   # left-right flip
        trm1.d = 1
        trm2.d = 1
    xlate1 = mupdf.fz_make_matrix(1, 0, 0, 1, -ch.m_internal.origin.x, -ch.m_internal.origin.y)
    xlate2 = mupdf.fz_make_matrix(1, 0, 0, 1, ch.m_internal.origin.x, ch.m_internal.origin.y)

    quad = mupdf.fz_transform_quad(mupdf.FzQuad(ch.m_internal.quad), xlate1)    # move origin to (0,0)
    quad = mupdf.fz_transform_quad(quad, trm1) # de-rotate corners
    
    # adjust vertical coordinates
    if c == 1 and quad.ul.y > 0:    # up-down flip
        quad.ul.y = asc
        quad.ur.y = asc
        quad.ll.y = dsc
        quad.lr.y = dsc
    else:
        quad.ul.y = -asc
        quad.ur.y = -asc
        quad.ll.y = -dsc
        quad.lr.y = -dsc

    # adjust horizontal coordinates that are too crazy:
    # (1) left x must be >= 0
    # (2) if bbox width is 0, lookup char advance in font.
    if quad.ll.x < 0:
        quad.ll.x = 0
        quad.ul.x = 0
    
    cwidth = quad.lr.x - quad.ll.x
    if cwidth < FLT_EPSILON:
        glyph = mupdf.fz_encode_character( font, ch.m_internal.c)
        if glyph:
            fwidth = mupdf.fz_advance_glyph( font, glyph, line.m_internal.wmode)
            quad.lr.x = quad.ll.x + fwidth * fsize
            quad.ur.x = quad.lr.x

    quad = mupdf.fz_transform_quad(quad, trm2) # rotate back
    quad = mupdf.fz_transform_quad(quad, xlate2)   # translate back
    return quad
