"""
Function: fitz.ConversionTrailer
Signature: ConversionTrailer(i: str)
Description: No docstring available.
"""

import fitz

# Source code of fitz.ConversionTrailer:
def ConversionTrailer(i: str):
    t = i.lower()
    text = ""
    json = "]\n}"
    html = "</body>\n</html>\n"
    xml = "</document>\n"
    xhtml = html
    if t == "html":
        r = html
    elif t == "json":
        r = json
    elif t == "xml":
        r = xml
    elif t == "xhtml":
        r = xhtml
    else:
        r = text

    return r
