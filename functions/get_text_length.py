"""
Function: fitz.get_text_length
Signature: get_text_length(text: str, fontname: str = 'helv', fontsize: float = 11, encoding: int = 0) -> float
Description:
Calculate length of a string for a built-in font.

Args:
    fontname: name of the font.
    fontsize: font size points.
    encoding: encoding to use, 0=Latin (default), 1=Greek, 2=Cyrillic.
Returns:
    (float) length of text.
"""

import fitz

# Source code of fitz.get_text_length:
def get_text_length(text: str, fontname: str ="helv", fontsize: float =11, encoding: int =0) -> float:
    """Calculate length of a string for a built-in font.

    Args:
        fontname: name of the font.
        fontsize: font size points.
        encoding: encoding to use, 0=Latin (default), 1=Greek, 2=Cyrillic.
    Returns:
        (float) length of text.
    """
    fontname = fontname.lower()
    basename = Base14_fontdict.get(fontname, None)

    glyphs = None
    if basename == "Symbol":
        glyphs = symbol_glyphs
    if basename == "ZapfDingbats":
        glyphs = zapf_glyphs
    if glyphs is not None:
        w = sum([glyphs[ord(c)][1] if ord(c) < 256 else glyphs[183][1] for c in text])
        return w * fontsize

    if fontname in Base14_fontdict.keys():
        return util_measure_string(
            text, Base14_fontdict[fontname], fontsize, encoding
        )

    if fontname in (
        "china-t",
        "china-s",
        "china-ts",
        "china-ss",
        "japan",
        "japan-s",
        "korea",
        "korea-s",
    ):
        return len(text) * fontsize

    raise ValueError("Font '%s' is unsupported" % fontname)
