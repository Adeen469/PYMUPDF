"""
Function: fitz.log
Signature: log(text='', caller=1)
Description:
For development/debugging diagnostics.
"""

import fitz

# Source code of fitz.log:
def log( text='', caller=1):
    '''
    For development/debugging diagnostics.
    '''
    try:
        stack = inspect.stack(context=0)
    except StopIteration:
        pass
    else:
        frame_record = stack[caller]
        try:
            filename = os.path.relpath(frame_record.filename)
        except Exception:   # Can fail on windows.
            filename = frame_record.filename
        line = frame_record.lineno
        function = frame_record.function
        text = f'{filename}:{line}:{function}(): {text}'
    if _g_log_items_active:
        _g_log_items.append(text)
    if _g_out_log:
        print(text, file=_g_out_log, flush=1)
