"""
Function: fitz.image_profile
Signature: image_profile(img: ByteString) -> dict
Description:
Return basic properties of an image.

Args:
    img: bytes, bytearray, io.BytesIO object or an opened image file.
Returns:
    A dictionary with keys width, height, colorspace.n, bpc, type, ext and size,
    where 'type' is the MuPDF image type (0 to 14) and 'ext' the suitable
    file extension.
"""

import fitz

# Source code of fitz.image_profile:
def image_profile(img: ByteString) -> dict:
    """ Return basic properties of an image.

    Args:
        img: bytes, bytearray, io.BytesIO object or an opened image file.
    Returns:
        A dictionary with keys width, height, colorspace.n, bpc, type, ext and size,
        where 'type' is the MuPDF image type (0 to 14) and 'ext' the suitable
        file extension.
    """
    if type(img) is io.BytesIO:
        stream = img.getvalue()
    elif hasattr(img, "read"):
        stream = img.read()
    elif type(img) in (bytes, bytearray):
        stream = img
    else:
        raise ValueError("bad argument 'img'")

    return TOOLS.image_profile(stream)
