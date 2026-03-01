"""
Function: fitz.getTJstr
Signature: getTJstr(text: str, glyphs: Union[list, tuple, NoneType], simple: bool, ordering: int) -> str
Description:
Return a PDF string enclosed in [] brackets, suitable for the PDF TJ
operator.

Notes:
    The input string is converted to either 2 or 4 hex digits per character.
Args:
    simple: no glyphs: 2-chars, use char codes as the glyph
            glyphs: 2-chars, use glyphs instead of char codes (Symbol,
            ZapfDingbats)
    not simple: ordering < 0: 4-chars, use glyphs not char codes
                ordering >=0: a CJK font! 4 chars, use char codes as glyphs
"""

import fitz

# Source code of fitz.getTJstr:
def getTJstr(text: str, glyphs: typing.Union[list, tuple, None], simple: bool, ordering: int) -> str:
    """ Return a PDF string enclosed in [] brackets, suitable for the PDF TJ
    operator.

    Notes:
        The input string is converted to either 2 or 4 hex digits per character.
    Args:
        simple: no glyphs: 2-chars, use char codes as the glyph
                glyphs: 2-chars, use glyphs instead of char codes (Symbol,
                ZapfDingbats)
        not simple: ordering < 0: 4-chars, use glyphs not char codes
                    ordering >=0: a CJK font! 4 chars, use char codes as glyphs
    """
    if text.startswith("[<") and text.endswith(">]"):  # already done
        return text

    if not bool(text):
        return "[<>]"

    if simple:  # each char or its glyph is coded as a 2-byte hex
        if glyphs is None:  # not Symbol, not ZapfDingbats: use char code
            otxt = "".join(["%02x" % ord(c) if ord(c) < 256 else "b7" for c in text])
        else:  # Symbol or ZapfDingbats: use glyphs
            otxt = "".join(
                ["%02x" % glyphs[ord(c)][0] if ord(c) < 256 else "b7" for c in text]
            )
        return "[<" + otxt + ">]"

    # non-simple fonts: each char or its glyph is coded as 4-byte hex
    if ordering < 0:  # not a CJK font: use the glyphs
        otxt = "".join(["%04x" % glyphs[ord(c)][0] for c in text])
    else:  # CJK: use the char codes
        otxt = "".join(["%04x" % ord(c) for c in text])

    return "[<" + otxt + ">]"
