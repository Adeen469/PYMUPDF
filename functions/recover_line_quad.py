"""
Function: fitz.recover_line_quad
Signature: recover_line_quad(line: dict, spans: list = None) -> pymupdf.Quad
Description:
Calculate the line quad for 'dict' / 'rawdict' text extractions.

The lower quad points are those of the first, resp. last span quad.
The upper points are determined by the maximum span quad height.
From this, compute a rect with bottom-left in (0, 0), convert this to a
quad and rotate and shift back to cover the text of the spans.

Args:
    spans: (list, optional) sub-list of spans to consider.
Returns:
    pymupdf.Quad covering selected spans.
"""

import fitz

# Source code of fitz.recover_line_quad:
def recover_line_quad(line: dict, spans: list = None) -> pymupdf.Quad:
    """Calculate the line quad for 'dict' / 'rawdict' text extractions.

    The lower quad points are those of the first, resp. last span quad.
    The upper points are determined by the maximum span quad height.
    From this, compute a rect with bottom-left in (0, 0), convert this to a
    quad and rotate and shift back to cover the text of the spans.

    Args:
        spans: (list, optional) sub-list of spans to consider.
    Returns:
        pymupdf.Quad covering selected spans.
    """
    if spans is None:  # no sub-selection
        spans = line["spans"]  # all spans
    if len(spans) == 0:
        raise ValueError("bad span list")
    line_dir = line["dir"]  # text direction
    cos, sin = line_dir
    q0 = recover_quad(line_dir, spans[0])  # quad of first span
    if len(spans) > 1:  # get quad of last span
        q1 = recover_quad(line_dir, spans[-1])
    else:
        q1 = q0  # last = first

    line_ll = q0.ll  # lower-left of line quad
    line_lr = q1.lr  # lower-right of line quad

    mat0 = pymupdf.planish_line(line_ll, line_lr)

    # map base line to x-axis such that line_ll goes to (0, 0)
    x_lr = line_lr * mat0

    small = pymupdf.TOOLS.set_small_glyph_heights()  # small glyph heights?

    h = max(
        [s["size"] * (1 if small else (s["ascender"] - s["descender"])) for s in spans]
    )

    line_rect = pymupdf.Rect(0, -h, x_lr.x, 0)  # line rectangle
    line_quad = line_rect.quad  # make it a quad and:
    line_quad *= ~mat0
    return line_quad
