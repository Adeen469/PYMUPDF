"""
Function: fitz.jm_dev_linewidth
Signature: jm_dev_linewidth(dev, ctx, path, stroke, matrix, colorspace, color, alpha, color_params)
Description: No docstring available.
"""

import fitz

# Source code of fitz.jm_dev_linewidth:
def jm_dev_linewidth( dev, ctx, path, stroke, matrix, colorspace, color, alpha, color_params):
    dev.linewidth = stroke.linewidth
    jm_increase_seqno( dev, ctx)
