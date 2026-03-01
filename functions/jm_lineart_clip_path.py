"""
Function: fitz.jm_lineart_clip_path
Signature: jm_lineart_clip_path(dev, ctx, path, even_odd, ctm, scissor)
Description: No docstring available.
"""

import fitz

# Source code of fitz.jm_lineart_clip_path:
def jm_lineart_clip_path(dev, ctx, path, even_odd, ctm, scissor):
    if not dev.clips:
        return
    dev.ctm = mupdf.FzMatrix(ctm)    # fz_concat(ctm, trace_device_ptm);
    dev.path_type = trace_device_CLIP_PATH
    jm_lineart_path(dev, ctx, path)
    if dev.pathdict is None:
        return
    dev.pathdict[ dictkey_type] = 'clip'
    dev.pathdict[ 'even_odd'] = bool(even_odd)
    if 'closePath' not in dev.pathdict:
        #log(f'setting dev.pathdict["closePath"] to False')
        dev.pathdict['closePath'] = False
   
    dev.pathdict['scissor'] = JM_py_from_rect(compute_scissor(dev))
    dev.pathdict['level'] = dev.depth
    dev.pathdict['layer'] = dev.layer_name
    jm_append_merge(dev)
    dev.depth += 1
