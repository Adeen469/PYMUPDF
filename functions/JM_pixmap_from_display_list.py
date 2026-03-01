"""
Function: fitz.JM_pixmap_from_display_list
Signature: JM_pixmap_from_display_list(list_, ctm, cs, alpha, clip, seps)
Description:
Version of fz_new_pixmap_from_display_list (util.c) to also support
rendering of only the 'clip' part of the displaylist rectangle
"""

import fitz

# Source code of fitz.JM_pixmap_from_display_list:
def JM_pixmap_from_display_list(
        list_,
        ctm,
        cs,
        alpha,
        clip,
        seps,
        ):
    '''
    Version of fz_new_pixmap_from_display_list (util.c) to also support
    rendering of only the 'clip' part of the displaylist rectangle
    '''
    assert isinstance(list_, mupdf.FzDisplayList)
    if seps is None:
        seps = mupdf.FzSeparations()
    assert seps is None or isinstance(seps, mupdf.FzSeparations), f'{type(seps)=}: {seps}'

    rect = mupdf.fz_bound_display_list(list_)
    matrix = JM_matrix_from_py(ctm)
    rclip = JM_rect_from_py(clip)
    rect = mupdf.fz_intersect_rect(rect, rclip)    # no-op if clip is not given

    rect = mupdf.fz_transform_rect(rect, matrix)
    irect = mupdf.fz_round_rect(rect)

    assert isinstance( cs, mupdf.FzColorspace)

    pix = mupdf.fz_new_pixmap_with_bbox(cs, irect, seps, alpha)
    if alpha:
        mupdf.fz_clear_pixmap(pix)
    else:
        mupdf.fz_clear_pixmap_with_value(pix, 0xFF)

    if not mupdf.fz_is_infinite_rect(rclip):
        dev = mupdf.fz_new_draw_device_with_bbox(matrix, pix, irect)
        mupdf.fz_run_display_list(list_, dev, mupdf.FzMatrix(), rclip, mupdf.FzCookie())
    else:
        dev = mupdf.fz_new_draw_device(matrix, pix)
        mupdf.fz_run_display_list(list_, dev, mupdf.FzMatrix(), mupdf.FzRect(mupdf.FzRect.Fixed_INFINITE), mupdf.FzCookie())

    mupdf.fz_close_device(dev)
    # Use special raw Pixmap constructor so we don't set alpha to true.
    return Pixmap( 'raw', pix)
