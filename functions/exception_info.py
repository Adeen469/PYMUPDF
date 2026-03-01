"""
Function: fitz.exception_info
Signature: exception_info()
Description: No docstring available.
"""

import fitz

# Source code of fitz.exception_info:
def exception_info():
    import traceback
    log(f'exception_info:')
    log(traceback.format_exc())
