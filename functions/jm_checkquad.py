"""
Function: fitz.jm_checkquad
Signature: jm_checkquad(dev)
Description:
Check whether the last 4 lines represent a quad.
Because of how we count, the lines are a polyline already, i.e. last point
of a line equals 1st point of next line.
So we check for a polygon (last line's end point equals start point).
If not true we return 0.
"""

import fitz

# Source code of fitz.jm_checkquad:
def jm_checkquad(dev):
    '''
    Check whether the last 4 lines represent a quad.
    Because of how we count, the lines are a polyline already, i.e. last point
    of a line equals 1st point of next line.
    So we check for a polygon (last line's end point equals start point).
    If not true we return 0.
    '''
    #log(f'{getattr(dev, "pathdict", None)=}')
    items = dev.pathdict[ dictkey_items]
    len_ = len(items)
    f = [0] * 8 # coordinates of the 4 corners
    # fill the 8 floats in f, start from items[-4:]
    for i in range( 4): # store line start points
        line = items[ len_ - 4 + i]
        temp = JM_point_from_py( line[1])
        f[i * 2] = temp.x
        f[i * 2 + 1] = temp.y
        lp = JM_point_from_py( line[ 2])
    if lp.x != f[0] or lp.y != f[1]:
        # not a polygon!
        #dev.linecount -= 1
        return 0
    
    # we have detected a quad
    dev.linecount = 0   # reset this
    # a quad item is ("qu", (ul, ur, ll, lr)), where the tuple items
    # are pairs of floats representing a quad corner each.
    
    # relationship of float array to quad points:
    # (0, 1) = ul, (2, 3) = ll, (6, 7) = ur, (4, 5) = lr
    q = mupdf.fz_make_quad(f[0], f[1], f[6], f[7], f[2], f[3], f[4], f[5])
    rect = ('qu', JM_py_from_quad(q))
    
    items[ len_ - 4] = rect  # replace item -4 by rect
    del items[ len_ - 3 : len_]  # delete remaining 3 items
    return 1
