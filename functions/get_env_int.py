"""
Function: fitz.get_env_int
Signature: get_env_int(name, default)
Description:
Returns `True`, `False` or `default` depending on whether $<name> is '1',
'0' or unset. Otherwise assert-fails.
"""

import fitz

# Source code of fitz.get_env_int:
def get_env_int( name, default):
    '''
    Returns `True`, `False` or `default` depending on whether $<name> is '1',
    '0' or unset. Otherwise assert-fails.
    '''
    v = os.environ.get( name)
    if v is None:
        ret = default
    else:
        ret = int(v)
    if ret != default:
        log(f'Using non-default setting from {name}: {v}')
    return ret
