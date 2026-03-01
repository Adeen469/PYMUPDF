"""
Function: fitz.RAISEPY
Signature: RAISEPY(msg, exc)
Description: No docstring available.
"""

import fitz

# Source code of fitz.RAISEPY:
def RAISEPY( msg, exc):
    #JM_Exc_CurrentException=exc
    #fz_throw(context, FZ_ERROR_GENERIC, msg)
    raise Exception( msg)
