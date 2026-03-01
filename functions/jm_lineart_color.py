"""
Function: fitz.jm_lineart_color
Signature: jm_lineart_color(colorspace, color)
Description: No docstring available.
"""

import fitz

# Source code of fitz.jm_lineart_color:
def jm_lineart_color(colorspace, color):
    #log(f' ')
    if colorspace:
        try:
            # Need to be careful to use a named Python object to ensure
            # that the `params` we pass to mupdf.ll_fz_convert_color() is
            # valid. E.g. doing:
            #
            #   rgb = mupdf.ll_fz_convert_color(..., mupdf.FzColorParams().internal())
            #
            # - seems to end up with a corrupted `params`.
            #
            cs = mupdf.FzColorspace( mupdf.FzColorspace.Fixed_RGB)
            cp = mupdf.FzColorParams()
            rgb = mupdf.ll_fz_convert_color(
                    colorspace,
                    color,
                    cs.m_internal,
                    None,
                    cp.internal(),
                    )
        except Exception:
            if g_exceptions_verbose:    exception_info()
            raise
        return rgb[:3]
    return ()
