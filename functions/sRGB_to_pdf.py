"""
Function: fitz.sRGB_to_pdf
Signature: sRGB_to_pdf(srgb: int) -> tuple
Description:
Convert sRGB color code to a PDF color triple.

There is **no error checking** for performance reasons!

Args:
    srgb: (int) RRGGBB (red, green, blue), each color in range(255).
Returns:
    Tuple (red, green, blue) each item in interval 0 <= item <= 1.
"""

import fitz

# Source code of fitz.sRGB_to_pdf:
def sRGB_to_pdf(srgb: int) -> tuple:
    """Convert sRGB color code to a PDF color triple.

    There is **no error checking** for performance reasons!

    Args:
        srgb: (int) RRGGBB (red, green, blue), each color in range(255).
    Returns:
        Tuple (red, green, blue) each item in interval 0 <= item <= 1.
    """
    t = sRGB_to_rgb(srgb)
    return t[0] / 255.0, t[1] / 255.0, t[2] / 255.0
