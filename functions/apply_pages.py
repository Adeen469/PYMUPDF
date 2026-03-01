"""
Function: fitz.apply_pages
Signature: apply_pages(path, pagefn, *, pagefn_args=(), pagefn_kwargs={}, initfn=None, initfn_args=(), initfn_kwargs={}, pages=None, method='single', concurrency=None, _stats=False)
Description:
Returns list of results from `pagefn()`, optionally using concurrency for
speed.

Args:
    path:
        Path of document.
    pagefn:
        Function to call for each page; is passed (page, *pagefn_args,
        **pagefn_kwargs). Return value is added to list that we return. If
        `method` is not 'single', must be a top-level function - nested
        functions don't work with concurrency.
    pagefn_args
    pagefn_kwargs:
        Additional args to pass to `pagefn`. Must be picklable.
    initfn:
        If true, called once in each worker process; is passed
        (*initfn_args, **initfn_kwargs).
    initfn_args
    initfn_kwargs:
        Args to pass to initfn. Must be picklable.
    pages:
        List of page numbers to process, or None to include all pages.
    method:
        'single'
            Do not use concurrency.
        'mp'
            Operate concurrently using Python's `multiprocessing` module.
        'fork'
             Operate concurrently using custom implementation with
             `os.fork()`. Does not work on Windows.
    concurrency:
        Number of worker processes to use when operating concurrently. If
        None, we use the number of available CPUs.
    _stats:
        Internal, may change or be removed. If true, we output simple
        timing diagnostics.

Note: We require a file path rather than a Document, because Document
instances do not work properly after a fork - internal file descriptor
offsets are shared between the parent and child processes.
"""

import fitz

# Source code of fitz.apply_pages:
def apply_pages(
        path,
        pagefn,
        *,
        pagefn_args=(),
        pagefn_kwargs=dict(),
        initfn=None,
        initfn_args=(),
        initfn_kwargs=dict(),
        pages=None,
        method='single',
        concurrency=None,
        _stats=False,
        ):
    '''
    Returns list of results from `pagefn()`, optionally using concurrency for
    speed.
    
    Args:
        path:
            Path of document.
        pagefn:
            Function to call for each page; is passed (page, *pagefn_args,
            **pagefn_kwargs). Return value is added to list that we return. If
            `method` is not 'single', must be a top-level function - nested
            functions don't work with concurrency.
        pagefn_args
        pagefn_kwargs:
            Additional args to pass to `pagefn`. Must be picklable.
        initfn:
            If true, called once in each worker process; is passed
            (*initfn_args, **initfn_kwargs).
        initfn_args
        initfn_kwargs:
            Args to pass to initfn. Must be picklable.
        pages:
            List of page numbers to process, or None to include all pages.
        method:
            'single'
                Do not use concurrency.
            'mp'
                Operate concurrently using Python's `multiprocessing` module.
            'fork'
                 Operate concurrently using custom implementation with
                 `os.fork()`. Does not work on Windows.
        concurrency:
            Number of worker processes to use when operating concurrently. If
            None, we use the number of available CPUs.
        _stats:
            Internal, may change or be removed. If true, we output simple
            timing diagnostics.
    
    Note: We require a file path rather than a Document, because Document
    instances do not work properly after a fork - internal file descriptor
    offsets are shared between the parent and child processes.
    '''
    if _stats:
        t0 = time.time()
    
    if method == 'single':
        if initfn:
            initfn(*initfn_args, **initfn_kwargs)
        ret = list()
        document = Document(path)
        if pages is None:
            pages = range(len(document))
        for pno in pages:
            page = document[pno]
            r = pagefn(page, *pagefn_args, **initfn_kwargs)
            ret.append(r)
    
    else:
        # Use concurrency.
        #
        from . import _apply_pages
    
        if pages is None:
            if _stats:
                t = time.time()
            with Document(path) as document:
                num_pages = len(document)
                pages = list(range(num_pages))
            if _stats:
                t = time.time() - t
                log(f'{t:.2f}s: count pages.')
    
        if _stats:
            t = time.time()
        
        if method == 'mp':
            ret = _apply_pages._multiprocessing(
                    path,
                    pages,
                    pagefn,
                    pagefn_args,
                    pagefn_kwargs,
                    initfn,
                    initfn_args,
                    initfn_kwargs,
                    concurrency,
                    _stats,
                    )
    
        elif method == 'fork':
            ret = _apply_pages._fork(
                    path,
                    pages,
                    pagefn,
                    pagefn_args,
                    pagefn_kwargs,
                    initfn,
                    initfn_args,
                    initfn_kwargs,
                    concurrency,
                    _stats,
                    )
        
        else:
            assert 0, f'Unrecognised {method=}.'
        
        if _stats:
            t = time.time() - t
            log(f'{t:.2f}s: work.')

    if _stats:
        t = time.time() - t0
        log(f'{t:.2f}s: total.')
    return ret
