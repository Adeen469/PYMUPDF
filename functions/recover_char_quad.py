"""
Function: fitz.recover_char_quad
Signature: recover_char_quad(line_dir: tuple, span: dict, char: dict) -> pymupdf.Quad
Description:
Recover the quadrilateral of a text character.

This requires the "rawdict" option of text extraction.

Args:
    line_dir: (tuple) 'line["dir"]' of the span's line.
    span: (dict) the span dict.
    char: (dict) the character dict.
Returns:
    The quadrilateral enveloping the character.
"""

import fitz

# Source code of fitz.recover_char_quad:
def recover_char_quad(line_dir: tuple, span: dict, char: dict) -> pymupdf.Quad:
    """Recover the quadrilateral of a text character.

    This requires the "rawdict" option of text extraction.

    Args:
        line_dir: (tuple) 'line["dir"]' of the span's line.
        span: (dict) the span dict.
        char: (dict) the character dict.
    Returns:
        The quadrilateral enveloping the character.
    """
    if line_dir is None:
        line_dir = span["dir"]
    if type(line_dir) is not tuple or len(line_dir) != 2:
        raise ValueError("bad line dir argument")
    if type(span) is not dict:
        raise ValueError("bad span argument")
    if type(char) is dict:
        bbox = pymupdf.Rect(char["bbox"])
    elif type(char) is tuple:
        bbox = pymupdf.Rect(char[3])
    else:
        raise ValueError("bad span argument")

    return recover_bbox_quad(line_dir, span, bbox)
