"""
Function: fitz.message
Signature: message(text='')
Description:
For user messages.
"""

import fitz

# Source code of fitz.message:
def message(text=''):
    '''
    For user messages.
    '''
    # It looks like `print()` does nothing if sys.stdout is None (without
    # raising an exception), but we don't rely on this.
    if _g_out_message:
        print(text, file=_g_out_message, flush=1)
