"""
Function: fitz.args_match
Signature: args_match(args, *types)
Description:
Returns true if <args> matches <types>.

Each item in <types> is a type or tuple of types. Any of these types will
match an item in <args>. `None` will match anything in <args>. `type(None)`
will match an arg whose value is `None`.
"""

import fitz

# Source code of fitz.args_match:
def args_match(args, *types):
    '''
    Returns true if <args> matches <types>.

    Each item in <types> is a type or tuple of types. Any of these types will
    match an item in <args>. `None` will match anything in <args>. `type(None)`
    will match an arg whose value is `None`.
    '''
    j = 0
    for i in range(len(types)):
        type_ = types[i]
        if j >= len(args):
            if isinstance(type_, tuple) and None in type_:
                # arg is missing but has default value.
                continue
            else:
                return False
        if type_ is not None and not isinstance(args[j], type_):
            return False
        j += 1
    if j != len(args):
        return False
    return True
