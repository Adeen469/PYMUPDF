"""
Function: fitz.make_table
Signature: make_table(rect: 'rect_like' = (0, 0, 1, 1), cols: int = 1, rows: int = 1) -> list
Description:
Return a list of (rows x cols) equal sized rectangles.

Notes:
    A utility to fill a given area with table cells of equal size.
Args:
    rect: rect_like to use as the table area
    rows: number of rows
    cols: number of columns
Returns:
    A list with <rows> items, where each item is a list of <cols>
    PyMuPDF Rect objects of equal sizes.
"""

import fitz

# Source code of fitz.make_table:
def make_table(rect: rect_like =(0, 0, 1, 1), cols: int =1, rows: int =1) -> list:
    """Return a list of (rows x cols) equal sized rectangles.

    Notes:
        A utility to fill a given area with table cells of equal size.
    Args:
        rect: rect_like to use as the table area
        rows: number of rows
        cols: number of columns
    Returns:
        A list with <rows> items, where each item is a list of <cols>
        PyMuPDF Rect objects of equal sizes.
    """
    rect = Rect(rect)  # ensure this is a Rect
    if rect.is_empty or rect.is_infinite:
        raise ValueError("rect must be finite and not empty")
    tl = rect.tl

    height = rect.height / rows  # height of one table cell
    width = rect.width / cols  # width of one table cell
    delta_h = (width, 0, width, 0)  # diff to next right rect
    delta_v = (0, height, 0, height)  # diff to next lower rect

    r = Rect(tl, tl.x + width, tl.y + height)  # first rectangle

    # make the first row
    row = [r]
    for i in range(1, cols):
        r += delta_h  # build next rect to the right
        row.append(r)

    # make result, starts with first row
    rects = [row]
    for i in range(1, rows):
        row = rects[i - 1]  # take previously appended row
        nrow = []  # the new row to append
        for r in row:  # for each previous cell add its downward copy
            nrow.append(r + delta_v)
        rects.append(nrow)  # append new row to result

    return rects
