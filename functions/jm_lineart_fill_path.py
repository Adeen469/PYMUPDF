"""
Function: fitz.jm_lineart_fill_path
Signature: jm_lineart_fill_path(dev, ctx, path, even_odd, ctm, colorspace, color, alpha, color_params)
Description: No docstring available.
"""

import fitz

# Source code of fitz.jm_lineart_fill_path:
def jm_lineart_fill_path( dev, ctx, path, even_odd, ctm, colorspace, color, alpha, color_params):
    #log(f'{getattr(dev, "pathdict", None)=}')
    #log(f'jm_lineart_fill_path(): {dev.seqno=}')
    even_odd = True if even_odd else False
    try:
        assert isinstance( ctm, mupdf.fz_matrix)
        dev.ctm = mupdf.FzMatrix( ctm)  # fz_concat(ctm, dev_ptm);
        dev.path_type = trace_device_FILL_PATH
        jm_lineart_path( dev, ctx, path)
        if dev.pathdict is None:
            return
        #item_count = len(dev.pathdict[ dictkey_items])
        #if item_count == 0:
        #    return
        dev.pathdict[ dictkey_type] ="f"
        dev.pathdict[ "even_odd"] = even_odd
        dev.pathdict[ "fill_opacity"] = alpha
        #log(f'setting dev.pathdict[ "closePath"] to false')
        #dev.pathdict[ "closePath"] = False
        dev.pathdict[ "fill"] = jm_lineart_color( colorspace, color)
        dev.pathdict[ dictkey_rect] = JM_py_from_rect(dev.pathrect)
        dev.pathdict[ "seqno"] = dev.seqno
        #jm_append_merge(dev)
        dev.pathdict[ 'layer'] = dev.layer_name
        if dev.clips:
            dev.pathdict[ 'level'] = dev.depth
        jm_append_merge(dev)
        dev.seqno += 1
        #log(f'jm_lineart_fill_path() end: {getattr(dev, "pathdict", None)=}')
    except Exception:
        if g_exceptions_verbose:    exception_info()
        raise
