"""
Function: fitz.jm_lineart_fill_text
Signature: jm_lineart_fill_text(dev, ctx, text, ctm, colorspace, color, alpha, color_params)
Description: No docstring available.
"""

import fitz

# Source code of fitz.jm_lineart_fill_text:
def jm_lineart_fill_text( dev, ctx, text, ctm, colorspace, color, alpha, color_params):
    if 0:
        log(f'{type(ctx)=} {ctx=}')
        log(f'{type(dev)=} {dev=}')
        log(f'{type(text)=} {text=}')
        log(f'{type(ctm)=} {ctm=}')
        log(f'{type(colorspace)=} {colorspace=}')
        log(f'{type(color)=} {color=}')
        log(f'{type(alpha)=} {alpha=}')
        log(f'{type(color_params)=} {color_params=}')
    jm_trace_text(dev, text, 0, ctm, colorspace, color, alpha, dev.seqno)
    dev.seqno += 1
