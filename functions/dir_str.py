"""
Function: fitz.dir_str
Signature: dir_str(x)
Description: No docstring available.
"""

import fitz

# Source code of fitz.dir_str:
def dir_str(x):
    ret = f'{x} {type(x)} ({len(dir(x))}):\n'
    for i in dir(x):
        ret += f'    {i}\n'
    return ret
