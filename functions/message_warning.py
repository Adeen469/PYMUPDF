"""
Function: fitz.message_warning
Signature: message_warning(text)
Description:
Generate a warning.
"""

import fitz

# Source code of fitz.message_warning:
def message_warning(text):
    '''
    Generate a warning.
    '''
    message(f'warning: {text}')
