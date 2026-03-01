"""
Function: fitz.format_g
Signature: format_g(value, *, fmt='%g')
Description:
Returns `value` formatted with mupdf.fz_format_double() if available,
otherwise with Python's `%`.

If `value` is a list or tuple, we return a space-separated string of
formatted values.
"""

import fitz

# Source code of fitz.format_g:
def _format_g(value, *, fmt='%g'):
    '''
    Returns `value` formatted with mupdf.fz_format_double() if available,
    otherwise with Python's `%`.

    If `value` is a list or tuple, we return a space-separated string of
    formatted values.
    '''
    if isinstance(value, (list, tuple)):
        ret = ''
        for v in value:
            if ret:
                ret += ' '
            ret += _format_g(v, fmt=fmt)
        return ret
    else:
        return mupdf.fz_format_double(fmt, value)
