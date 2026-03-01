"""
Function: fitz.jm_checkrect
Signature: jm_checkrect(dev)
Description:
Check whether the last 3 path items represent a rectangle.
Returns 1 if we have modified the path, otherwise 0.
"""

import fitz

# Source code of fitz.jm_checkrect:
def jm_checkrect(dev):
    '''
    Check whether the last 3 path items represent a rectangle.
    Returns 1 if we have modified the path, otherwise 0.
    '''
    #log(f'{getattr(dev, "pathdict", None)=}')
    dev.linecount = 0   # reset line count
    orientation = 0 # area orientation of rectangle
    items = dev.pathdict[ dictkey_items]
    len_ = len(items)

    line0 = items[ len_ - 3]
    ll = JM_point_from_py( line0[ 1])
    lr = JM_point_from_py( line0[ 2])

    # no need to extract "line1"!
    line2 = items[ len_ - 1]
    ur = JM_point_from_py( line2[ 1])
    ul = JM_point_from_py( line2[ 2])

    # Assumption:
    # When decomposing rects, MuPDF always starts with a horizontal line,
    # followed by a vertical line, followed by a horizontal line.
    # First line: (ll, lr), third line: (ul, ur).
    # If 1st line is below 3rd line, we record anti-clockwise (+1), else
    # clockwise (-1) orientation.
    
    if (0
            or ll.y != lr.y
            or ll.x != ul.x
            or ur.y != ul.y
            or ur.x != lr.x
            ):
        return 0 # not a rectangle
    
    # we have a rect, replace last 3 "l" items by one "re" item.
    if ul.y < lr.y:
        r = mupdf.fz_make_rect(ul.x, ul.y, lr.x, lr.y)
        orientation = 1
    else:
        r = mupdf.fz_make_rect(ll.x, ll.y, ur.x, ur.y)
        orientation = -1
    
    rect = ( 're', JM_py_from_rect(r), orientation)
    items[ len_ - 3] = rect # replace item -3 by rect
    del items[ len_ - 2 : len_] # delete remaining 2 items
    return 1
