"""
Function: fitz.jm_lineart_path
Signature: jm_lineart_path(dev, ctx, path)
Description:
Create the "items" list of the path dictionary
* either create or empty the path dictionary
* reset the end point of the path
* reset count of consecutive lines
* invoke fz_walk_path(), which create the single items
* if no items detected, empty path dict again
"""

import fitz

# Source code of fitz.jm_lineart_path:
def jm_lineart_path(dev, ctx, path):
    '''
    Create the "items" list of the path dictionary
    * either create or empty the path dictionary
    * reset the end point of the path
    * reset count of consecutive lines
    * invoke fz_walk_path(), which create the single items
    * if no items detected, empty path dict again
    '''
    #log(f'{getattr(dev, "pathdict", None)=}')
    try:
        dev.pathrect = mupdf.FzRect( mupdf.FzRect.Fixed_INFINITE)
        dev.linecount = 0
        dev.lastpoint = mupdf.FzPoint( 0, 0)
        dev.pathdict = dict()
        dev.pathdict[ dictkey_items] = []
        
        # First time we create a Walker instance is slow, e.g. 0.3s, then later
        # times run in around 0.01ms. If Walker is defined locally instead of
        # globally, each time takes 0.3s.
        #
        walker = Walker(dev)
        # Unlike fz_run_page(), fz_path_walker callbacks are not passed
        # a pointer to the struct, instead they get an arbitrary
        # void*. The underlying C++ Director callbacks use this void* to
        # identify the fz_path_walker instance so in turn we need to pass
        # arg=walker.m_internal.
        mupdf.fz_walk_path( mupdf.FzPath(mupdf.ll_fz_keep_path(path)), walker, walker.m_internal)
        # Check if any items were added ...
        if not dev.pathdict[ dictkey_items]:
            dev.pathdict = None
    except Exception:
        if g_exceptions_verbose:    exception_info()
        raise
