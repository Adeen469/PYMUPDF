"""
Function: fitz.JM_pixmap_from_page
Signature: JM_pixmap_from_page(doc, page, ctm, cs, alpha, annots, clip)
Description:
Pixmap creation directly using a short-lived displaylist, so we can support
separations.
"""

import fitz

# Source code of fitz.JM_pixmap_from_page:
def JM_pixmap_from_page(doc, page, ctm, cs, alpha, annots, clip):
    '''
    Pixmap creation directly using a short-lived displaylist, so we can support
    separations.
    '''
    SPOTS_NONE = 0
    SPOTS_OVERPRINT_SIM = 1
    SPOTS_FULL = 2
    
    FZ_ENABLE_SPOT_RENDERING = True # fixme: this is a build-time setting in MuPDF's config.h.
    if FZ_ENABLE_SPOT_RENDERING:
        spots = SPOTS_OVERPRINT_SIM
    else:
        spots = SPOTS_NONE

    seps = None
    colorspace = cs
    
    matrix = JM_matrix_from_py(ctm)
    rect = mupdf.fz_bound_page(page)
    rclip = JM_rect_from_py(clip)
    rect = mupdf.fz_intersect_rect(rect, rclip) # no-op if clip is not given
    rect = mupdf.fz_transform_rect(rect, matrix)
    bbox = mupdf.fz_round_rect(rect)

    # Pixmap of the document's /OutputIntents ("output intents")
    oi = mupdf.fz_document_output_intent(doc)
    # if present and compatible, use it instead of the parameter
    if oi.m_internal:
        if mupdf.fz_colorspace_n(oi) == mupdf.fz_colorspace_n(cs):
            colorspace = mupdf.fz_keep_colorspace(oi)

    # check if spots rendering is available and if so use separations
    if spots != SPOTS_NONE:
        seps = mupdf.fz_page_separations(page)
        if seps.m_internal:
            n = mupdf.fz_count_separations(seps)
            if spots == SPOTS_FULL:
                for i in range(n):
                    mupdf.fz_set_separation_behavior(seps, i, mupdf.FZ_SEPARATION_SPOT)
            else:
                for i in range(n):
                    mupdf.fz_set_separation_behavior(seps, i, mupdf.FZ_SEPARATION_COMPOSITE)
        elif mupdf.fz_page_uses_overprint(page):
            # This page uses overprint, so we need an empty
            # sep object to force the overprint simulation on.
            seps = mupdf.fz_new_separations(0)
        elif oi.m_internal and mupdf.fz_colorspace_n(oi) != mupdf.fz_colorspace_n(colorspace):
            # We have an output intent, and it's incompatible
            # with the colorspace our device needs. Force the
            # overprint simulation on, because this ensures that
            # we 'simulate' the output intent too.
            seps = mupdf.fz_new_separations(0)

    pix = mupdf.fz_new_pixmap_with_bbox(colorspace, bbox, seps, alpha)

    if alpha:
        mupdf.fz_clear_pixmap(pix)
    else:
        mupdf.fz_clear_pixmap_with_value(pix, 0xFF)

    dev = mupdf.fz_new_draw_device(matrix, pix)
    if annots:
        mupdf.fz_run_page(page, dev, mupdf.FzMatrix(), mupdf.FzCookie())
    else:
        mupdf.fz_run_page_contents(page, dev, mupdf.FzMatrix(), mupdf.FzCookie())
    mupdf.fz_close_device(dev)
    return pix
