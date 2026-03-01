"""
Function: fitz.get_text
Signature: get_text(path, *, pages=None, method='single', concurrency=None, option='text', clip=None, flags=None, textpage=None, sort=False, delimiters=None, _stats=False)
Description:
Returns list of results from `Page.get_text()`, optionally using
concurrency for speed.

Args:
    path:
        Path of document.
    pages:
        List of page numbers to process, or None to include all pages.
    method:
        'single'
            Do not use concurrency.
        'mp'
            Operate concurrently using Python's `multiprocessing` module.
        'fork'
             Operate concurrently using custom implementation with
             `os.fork`. Does not work on Windows.
    concurrency:
        Number of worker processes to use when operating concurrently. If
        None, we use the number of available CPUs.
    option
    clip
    flags
    textpage
    sort
    delimiters:
        Passed to internal calls to `Page.get_text()`.
"""

import fitz

# Source code of fitz.get_text:
def get_text(
        path,
        *,
        pages=None,
        method='single',
        concurrency=None,
        
        option='text',
        clip=None,
        flags=None,
        textpage=None,
        sort=False,
        delimiters=None,
        
        _stats=False,
        ):
    '''
    Returns list of results from `Page.get_text()`, optionally using
    concurrency for speed.
    
    Args:
        path:
            Path of document.
        pages:
            List of page numbers to process, or None to include all pages.
        method:
            'single'
                Do not use concurrency.
            'mp'
                Operate concurrently using Python's `multiprocessing` module.
            'fork'
                 Operate concurrently using custom implementation with
                 `os.fork`. Does not work on Windows.
        concurrency:
            Number of worker processes to use when operating concurrently. If
            None, we use the number of available CPUs.
        option
        clip
        flags
        textpage
        sort
        delimiters:
            Passed to internal calls to `Page.get_text()`.
    '''
    args_dict = dict(
            option=option,
            clip=clip,
            flags=flags,
            textpage=textpage,
            sort=sort,
            delimiters=delimiters,
            )
    
    return apply_pages(
            path,
            Page.get_text,
            pagefn_kwargs=args_dict,
            pages=pages,
            method=method,
            concurrency=concurrency,
            _stats=_stats,
            )
