"""
Function: fitz.paper_size
Signature: paper_size(s: str) -> tuple
Description:
Return a tuple (width, height) for a given paper format string.

Notes:
    'A4-L' will return (842, 595), the values for A4 landscape.
    Suffix '-P' and no suffix return the portrait tuple.
"""

import fitz

# Source code of fitz.paper_size:
def paper_size(s: str) -> tuple:
    """Return a tuple (width, height) for a given paper format string.

    Notes:
        'A4-L' will return (842, 595), the values for A4 landscape.
        Suffix '-P' and no suffix return the portrait tuple.
    """
    size = s.lower()
    f = "p"
    if size.endswith("-l"):
        f = "l"
        size = size[:-2]
    if size.endswith("-p"):
        size = size[:-2]
    rc = paper_sizes().get(size, (-1, -1))
    if f == "p":
        return rc
    return (rc[1], rc[0])
