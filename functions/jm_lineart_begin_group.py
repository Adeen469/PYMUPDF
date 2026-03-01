"""
Function: fitz.jm_lineart_begin_group
Signature: jm_lineart_begin_group(dev, ctx, bbox, cs, isolated, knockout, blendmode, alpha)
Description: No docstring available.
"""

import fitz

# Source code of fitz.jm_lineart_begin_group:
def jm_lineart_begin_group(dev, ctx, bbox, cs, isolated, knockout, blendmode, alpha):
    #log(f'{dev.pathdict=} {dev.clips=}')
    if not dev.clips:
        return
    dev.pathdict = { # Py_BuildValue("{s:s,s:N,s:N,s:N,s:s,s:f,s:i,s:N}",
            "type": "group",
            "rect": JM_py_from_rect(bbox),
            "isolated": bool(isolated),
            "knockout": bool(knockout),
            "blendmode": mupdf.fz_blendmode_name(blendmode),
            "opacity": alpha,
            "level": dev.depth,
            "layer": dev.layer_name
            }
    jm_append_merge(dev)
    dev.depth += 1
