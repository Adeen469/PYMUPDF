"""
Function: fitz.jm_append_merge
Signature: jm_append_merge(dev)
Description:
Append current path to list or merge into last path of the list.
(1) Append if first path, different item lists or not a 'stroke' version
    of previous path
(2) If new path has the same items, merge its content into previous path
    and change path["type"] to "fs".
(3) If "out" is callable, skip the previous and pass dictionary to it.
"""

import fitz

# Source code of fitz.jm_append_merge:
def jm_append_merge(dev):
    '''
    Append current path to list or merge into last path of the list.
    (1) Append if first path, different item lists or not a 'stroke' version
        of previous path
    (2) If new path has the same items, merge its content into previous path
        and change path["type"] to "fs".
    (3) If "out" is callable, skip the previous and pass dictionary to it.
    '''
    #log(f'{getattr(dev, "pathdict", None)=}')
    assert isinstance(dev.out, list)
    #log( f'{dev.out=}')
    
    if callable(dev.method) or dev.method:  # function or method
        # callback.
        if dev.method is None:
            # fixme, this surely cannot happen?
            assert 0
            #resp = PyObject_CallFunctionObjArgs(out, dev.pathdict, NULL)
        else:
            #log(f'calling {dev.out=} {dev.method=} {dev.pathdict=}')
            resp = getattr(dev.out, dev.method)(dev.pathdict)
        if not resp:
            message("calling cdrawings callback function/method failed!")
        dev.pathdict = None
        return
    
    def append():
        #log(f'jm_append_merge(): clearing dev.pathdict')
        dev.out.append(dev.pathdict.copy())
        dev.pathdict.clear()
    assert isinstance(dev.out, list)
    len_ = len(dev.out) # len of output list so far
    #log('{len_=}')
    if len_ == 0:   # always append first path
        return append()
    #log(f'{getattr(dev, "pathdict", None)=}')
    thistype = dev.pathdict[ dictkey_type]
    #log(f'{thistype=}')
    if thistype != 's': # if not stroke, then append
        return append()
    prev = dev.out[ len_-1] # get prev path
    #log( f'{prev=}')
    prevtype = prev[ dictkey_type]
    #log( f'{prevtype=}')
    if prevtype != 'f': # if previous not fill, append
        return append()
    # last check: there must be the same list of items for "f" and "s".
    previtems = prev[ dictkey_items]
    thisitems = dev.pathdict[ dictkey_items]
    if previtems != thisitems:
        return append()
    
    #rc = PyDict_Merge(prev, dev.pathdict, 0);  // merge with no override
    try:
        for k, v in dev.pathdict.items():
            if k not in prev:
                prev[k] = v
        rc = 0
    except Exception:
        if g_exceptions_verbose:    exception_info()
        #raise
        rc = -1
    if rc == 0:
        prev[ dictkey_type] = 'fs'
        dev.pathdict.clear()
    else:
        message("could not merge stroke and fill path")
        append()
