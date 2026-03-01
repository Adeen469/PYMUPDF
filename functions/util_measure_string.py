"""
Function: fitz.util_measure_string
Signature: util_measure_string(text, fontname, fontsize, encoding)
Description: No docstring available.
"""

import fitz

# Source code of fitz.util_measure_string:
def util_measure_string( text, fontname, fontsize, encoding):
    font = mupdf.fz_new_base14_font(fontname)
    w = 0
    pos = 0
    while pos < len(text):
        t, c = mupdf.fz_chartorune(text[pos:])
        pos += t
        if encoding == mupdf.PDF_SIMPLE_ENCODING_GREEK:
            c = mupdf.fz_iso8859_7_from_unicode(c)
        elif encoding == mupdf.PDF_SIMPLE_ENCODING_CYRILLIC:
            c = mupdf.fz_windows_1251_from_unicode(c)
        else:
            c = mupdf.fz_windows_1252_from_unicode(c)
        if c < 0:
            c = 0xB7
        g = mupdf.fz_encode_character(font, c)
        dw = mupdf.fz_advance_glyph(font, g, 0)
        w += dw
    ret = w * fontsize
    return ret
