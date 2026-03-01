"""
Function: fitz.recover_span_quad
Signature: recover_span_quad(line_dir: tuple, span: dict, chars: list = None) -> pymupdf.Quad
Description:
Calculate the span quad for 'dict' / 'rawdict' text extractions.

Notes:
    There are two execution paths:
    1. For the full span quad, the result of 'recover_quad' is returned.
    2. For the quad of a sub-list of characters, the char quads are
       computed and joined. This is only supported for the "rawdict"
       extraction option.

Args:
    line_dir: (tuple) 'line["dir"]' of the owning line.
    span: (dict) the span.
    chars: (list, optional) sub-list of characters to consider.
Returns:
    pymupdf.Quad covering selected characters.
"""

import fitz

# Source code of fitz.recover_span_quad:
def recover_span_quad(line_dir: tuple, span: dict, chars: list = None) -> pymupdf.Quad:
    """Calculate the span quad for 'dict' / 'rawdict' text extractions.

    Notes:
        There are two execution paths:
        1. For the full span quad, the result of 'recover_quad' is returned.
        2. For the quad of a sub-list of characters, the char quads are
           computed and joined. This is only supported for the "rawdict"
           extraction option.

    Args:
        line_dir: (tuple) 'line["dir"]' of the owning line.
        span: (dict) the span.
        chars: (list, optional) sub-list of characters to consider.
    Returns:
        pymupdf.Quad covering selected characters.
    """
    if line_dir is None:  # must be a span from get_texttrace()
        line_dir = span["dir"]
    if chars is None:  # no sub-selection
        return recover_quad(line_dir, span)
    if "chars" not in span.keys():
        raise ValueError("need 'rawdict' option to sub-select chars")

    q0 = recover_char_quad(line_dir, span, chars[0])  # quad of first char
    if len(chars) > 1:  # get quad of last char
        q1 = recover_char_quad(line_dir, span, chars[-1])
    else:
        q1 = q0  # last = first

    span_ll = q0.ll  # lower-left of span quad
    span_lr = q1.lr  # lower-right of span quad
    mat0 = pymupdf.planish_line(span_ll, span_lr)
    # map base line to x-axis such that span_ll goes to (0, 0)
    x_lr = span_lr * mat0

    small = pymupdf.TOOLS.set_small_glyph_heights()  # small glyph heights?
    h = span["size"] * (1 if small else (span["ascender"] - span["descender"]))

    span_rect = pymupdf.Rect(0, -h, x_lr.x, 0)  # line rectangle
    span_quad = span_rect.quad  # make it a quad and:
    span_quad *= ~mat0  # rotate back and shift back
    return span_quad
