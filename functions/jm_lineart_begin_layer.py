"""
Function: fitz.jm_lineart_begin_layer
Signature: jm_lineart_begin_layer(dev, ctx, name)
Description: No docstring available.
"""

import fitz

# Source code of fitz.jm_lineart_begin_layer:
def jm_lineart_begin_layer(dev, ctx, name):
    if name:
        dev.layer_name = name
    else:
        dev.layer_name = ""
