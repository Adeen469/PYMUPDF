"""
Function: fitz.set_messages
Signature: set_messages(*, text=None, fd=None, stream=None, path=None, path_append=None, pylogging=None, pylogging_logger=None, pylogging_level=None, pylogging_name=None)
Description:
Sets destination of PyMuPDF messages. See _make_output() for details.
"""

import fitz

# Source code of fitz.set_messages:
def set_messages(
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
    Sets destination of PyMuPDF messages. See _make_output() for details.
    '''
    global _g_out_message
    _g_out_message = _make_output(
            text=text,
            fd=fd,
            stream=stream,
            path=path,
            path_append=path_append,
            pylogging=pylogging,
            pylogging_logger=pylogging_logger,
            pylogging_level=pylogging_level,
            pylogging_name=pylogging_name,
            default=_g_out_message,
            )
