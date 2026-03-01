"""
Function: fitz.jm_lineart_stroke_path
Signature: jm_lineart_stroke_path(dev, ctx, path, stroke, ctm, colorspace, color, alpha, color_params)
Description: No docstring available.
"""

import fitz

# Source code of fitz.jm_lineart_stroke_path:
def jm_lineart_stroke_path( dev, ctx, path, stroke, ctm, colorspace, color, alpha, color_params):
    #log(f'{dev.pathdict=} {dev.clips=}')
    try:
        assert isinstance( ctm, mupdf.fz_matrix)
        dev.pathfactor = 1
        if ctm.a != 0 and abs(ctm.a) == abs(ctm.d):
            dev.pathfactor = abs(ctm.a)
        elif ctm.b != 0 and abs(ctm.b) == abs(ctm.c):
            dev.pathfactor = abs(ctm.b)
        dev.ctm = mupdf.FzMatrix( ctm)  # fz_concat(ctm, dev_ptm);
        dev.path_type = trace_device_STROKE_PATH

        jm_lineart_path( dev, ctx, path)
        if dev.pathdict is None:
            return
        dev.pathdict[ dictkey_type] = 's'
        dev.pathdict[ 'stroke_opacity'] = alpha
        dev.pathdict[ 'color'] = jm_lineart_color( colorspace, color)
        dev.pathdict[ dictkey_width] = dev.pathfactor * stroke.linewidth
        dev.pathdict[ 'lineCap'] = (
                stroke.start_cap,
                stroke.dash_cap,
                stroke.end_cap,
                )
        dev.pathdict[ 'lineJoin'] = dev.pathfactor * stroke.linejoin
        if 'closePath' not in dev.pathdict:
            #log('setting dev.pathdict["closePath"] to false')
            dev.pathdict['closePath'] = False

        # output the "dashes" string
        if stroke.dash_len:
            buff = mupdf.fz_new_buffer( 256)
            mupdf.fz_append_string( buff, "[ ") # left bracket
            for i in range( stroke.dash_len):
                # We use mupdf python's SWIG-generated floats_getitem() fn to
                # access float *stroke.dash_list[].
                value = mupdf.floats_getitem( stroke.dash_list, i)  # stroke.dash_list[i].
                mupdf.fz_append_string( buff, f'{_format_g(dev.pathfactor * value)} ')
            mupdf.fz_append_string( buff, f'] {_format_g(dev.pathfactor * stroke.dash_phase)}')
            dev.pathdict[ 'dashes'] = buff
        else:
            dev.pathdict[ 'dashes'] = '[] 0'
        dev.pathdict[ dictkey_rect] = JM_py_from_rect(dev.pathrect)
        dev.pathdict['layer'] = dev.layer_name
        dev.pathdict[ 'seqno'] = dev.seqno
        if dev.clips:
            dev.pathdict[ 'level'] = dev.depth
        jm_append_merge(dev)
        dev.seqno += 1
    
    except Exception:
        if g_exceptions_verbose:    exception_info()
        raise
