"""
Function: fitz.get_highlight_selection
Signature: get_highlight_selection(page, start: 'point_like' = None, stop: 'point_like' = None, clip: 'rect_like' = None) -> list
Description:
Return rectangles of text lines between two points.

Notes:
    The default of 'start' is top-left of 'clip'. The default of 'stop'
    is bottom-reight of 'clip'.

Args:
    start: start point_like
    stop: end point_like, must be 'below' start
    clip: consider this rect_like only, default is page rectangle
Returns:
    List of line bbox intersections with the area established by the
    parameters.
"""

import fitz

# Source code of fitz.get_highlight_selection:
def get_highlight_selection(page, start: point_like =None, stop: point_like =None, clip: rect_like =None) -> list:
    """Return rectangles of text lines between two points.

    Notes:
        The default of 'start' is top-left of 'clip'. The default of 'stop'
        is bottom-reight of 'clip'.

    Args:
        start: start point_like
        stop: end point_like, must be 'below' start
        clip: consider this rect_like only, default is page rectangle
    Returns:
        List of line bbox intersections with the area established by the
        parameters.
    """
    # validate and normalize arguments
    if clip is None:
        clip = page.rect
    clip = Rect(clip)
    if start is None:
        start = clip.tl
    if stop is None:
        stop = clip.br
    clip.y0 = start.y
    clip.y1 = stop.y
    if clip.is_empty or clip.is_infinite:
        return []

    # extract text of page, clip only, no images, expand ligatures
    blocks = page.get_text(
        "dict", flags=0, clip=clip,
    )["blocks"]

    lines = []  # will return this list of rectangles
    for b in blocks:
        bbox = Rect(b["bbox"])
        if bbox.is_infinite or bbox.is_empty:
            continue
        for line in b["lines"]:
            bbox = Rect(line["bbox"])
            if bbox.is_infinite or bbox.is_empty:
                continue
            lines.append(bbox)

    if lines == []:  # did not select anything
        return lines

    lines.sort(key=lambda bbox: bbox.y1)  # sort by vertical positions

    # cut off prefix from first line if start point is close to its top
    bboxf = lines.pop(0)
    if bboxf.y0 - start.y <= 0.1 * bboxf.height:  # close enough?
        r = Rect(start.x, bboxf.y0, bboxf.br)  # intersection rectangle
        if not (r.is_empty or r.is_infinite):
            lines.insert(0, r)  # insert again if not empty
    else:
        lines.insert(0, bboxf)  # insert again

    if lines == []:  # the list might have been emptied
        return lines

    # cut off suffix from last line if stop point is close to its bottom
    bboxl = lines.pop()
    if stop.y - bboxl.y1 <= 0.1 * bboxl.height:  # close enough?
        r = Rect(bboxl.tl, stop.x, bboxl.y1)  # intersection rectangle
        if not (r.is_empty or r.is_infinite):
            lines.append(r)  # append if not empty
    else:
        lines.append(bboxl)  # append again

    return lines
