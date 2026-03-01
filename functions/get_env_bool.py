"""
Function: fitz.get_env_bool
Signature: get_env_bool(name, default)
Description:
Returns `True`, `False` or `default` depending on whether $<name> is '1',
'0' or unset. Otherwise assert-fails.
"""

import fitz

# Source code of fitz.get_env_bool:
def get_env_bool( name, default):
    '''
    Returns `True`, `False` or `default` depending on whether $<name> is '1',
    '0' or unset. Otherwise assert-fails.
    '''
    v = os.environ.get( name)
    if v is None:
        ret = default
    elif v == '1':
        ret = True
    elif v == '0':
        ret = False
    else:
        assert 0, f'Unrecognised value for {name}: {v!r}'
    if ret != default:
        log(f'Using non-default setting from {name}: {v!r}')
    return ret
