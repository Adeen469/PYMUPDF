"""
Function: fitz.jm_lineart_end_group
Signature: jm_lineart_end_group(dev, ctx)
Description: No docstring available.
"""

import fitz

# Source code of fitz.jm_lineart_end_group:
def jm_lineart_end_group(dev, ctx):
    #log(f'{dev.pathdict=} {dev.clips=}')
    if not dev.clips:
        return
    dev.depth -= 1
