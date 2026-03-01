"""
Function: fitz.set_log
Signature: set_log(*, text=None, fd=None, stream=None, path=None, path_append=None, pylogging=None, pylogging_logger=None, pylogging_level=None, pylogging_name=None)
Description:
Sets destination of PyMuPDF development/debugging logging. See
_make_output() for details.
"""

import fitz

# Source code of fitz.set_log:
def set_log(
        *,
        text=None,
        fd=None,
        stream=None,
        path=None,
        path_append=None,
        pylogging=None,
        pylogging_logger=None,
        pylogging_level=None,
        pylogging_name=None,
        ):
    '''
    Sets destination of PyMuPDF development/debugging logging. See
    _make_output() for details.
    '''
    global _g_out_log
    _g_out_log = _make_output(
            text=text,
            fd=fd,
            stream=stream,
            path=path,
            path_append=path_append,
            pylogging=pylogging,
            pylogging_logger=pylogging_logger,
            pylogging_level=pylogging_level,
            pylogging_name=pylogging_name,
            default=_g_out_log,
            )
