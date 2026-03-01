"""
Function: fitz.sRGB_to_rgb
Signature: sRGB_to_rgb(srgb: int) -> tuple
Description:
Convert sRGB color code to an RGB color triple.

There is **no error checking** for performance reasons!

Args:
    srgb: (int) SSRRGGBB (red, green, blue), each color in range(255).
    With MuPDF < 1.26, `s` is always 0.
Returns:
    Tuple (red, green, blue) each item in interval 0 <= item <= 255.
"""

import fitz

# Source code of fitz.sRGB_to_rgb:
def sRGB_to_rgb(srgb: int) -> tuple:
    """Convert sRGB color code to an RGB color triple.

    There is **no error checking** for performance reasons!

    Args:
        srgb: (int) SSRRGGBB (red, green, blue), each color in range(255).
        With MuPDF < 1.26, `s` is always 0.
    Returns:
        Tuple (red, green, blue) each item in interval 0 <= item <= 255.
    """
    srgb &= 0xffffff
    r = srgb >> 16
    g = (srgb - (r << 16)) >> 8
    b = srgb - (r << 16) - (g << 8)
    return (r, g, b)
