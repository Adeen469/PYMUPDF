"""
Function: fitz.jm_lineart_drop_device
Signature: jm_lineart_drop_device(dev, ctx)
Description: No docstring available.
"""

import fitz

# Source code of fitz.jm_lineart_drop_device:
def jm_lineart_drop_device(dev, ctx):
    if isinstance(dev.out, list):
        dev.out = []
    dev.scissors = []
