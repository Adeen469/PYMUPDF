"""
Function: fitz.recover_bbox_quad
Signature: recover_bbox_quad(line_dir: tuple, span: dict, bbox: tuple) -> pymupdf.Quad
Description:
Compute the quad located inside the bbox.

The bbox may be any of the resp. tuples occurring inside the given span.

Args:
    line_dir: (tuple) 'line["dir"]' of the owning line or None.
    span: (dict) the span. May be from get_texttrace() method.
    bbox: (tuple) the bbox of the span or any of its characters.
Returns:
    The quad which is wrapped by the bbox.
"""

import fitz

# Source code of fitz.recover_bbox_quad:
def recover_bbox_quad(line_dir: tuple, span: dict, bbox: tuple) -> pymupdf.Quad:
    """Compute the quad located inside the bbox.

    The bbox may be any of the resp. tuples occurring inside the given span.

    Args:
        line_dir: (tuple) 'line["dir"]' of the owning line or None.
        span: (dict) the span. May be from get_texttrace() method.
        bbox: (tuple) the bbox of the span or any of its characters.
    Returns:
        The quad which is wrapped by the bbox.
    """
    if line_dir is None:
        line_dir = span["dir"]
    cos, sin = line_dir
    bbox = pymupdf.Rect(bbox)  # make it a rect
    if pymupdf.TOOLS.set_small_glyph_heights():  # ==> just fontsize as height
        d = 1
    else:
        d = span["ascender"] - span["descender"]

    height = d * span["size"]  # the quad's rectangle height
    # The following are distances from the bbox corners, at which we find the
    # respective quad points. The computation depends on in which quadrant the
    # text writing angle is located.
    hs = height * sin
    hc = height * cos
    if hc >= 0 and hs <= 0:  # quadrant 1
        ul = bbox.bl - (0, hc)
        ur = bbox.tr + (hs, 0)
        ll = bbox.bl - (hs, 0)
        lr = bbox.tr + (0, hc)
    elif hc <= 0 and hs <= 0:  # quadrant 2
        ul = bbox.br + (hs, 0)
        ur = bbox.tl - (0, hc)
        ll = bbox.br + (0, hc)
        lr = bbox.tl - (hs, 0)
    elif hc <= 0 and hs >= 0:  # quadrant 3
        ul = bbox.tr - (0, hc)
        ur = bbox.bl + (hs, 0)
        ll = bbox.tr - (hs, 0)
        lr = bbox.bl + (0, hc)
    else:  # quadrant 4
        ul = bbox.tl + (hs, 0)
        ur = bbox.br - (0, hc)
        ll = bbox.tl + (0, hc)
        lr = bbox.br - (hs, 0)
    return pymupdf.Quad(ul, ur, ll, lr)
