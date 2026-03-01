"""
Function: fitz.ConversionHeader
Signature: ConversionHeader(i: str, filename: Optional[str] = 'unknown')
Description: No docstring available.
"""

import fitz

# Source code of fitz.ConversionHeader:
def ConversionHeader(i: str, filename: OptStr ="unknown"):
    t = i.lower()
    import textwrap
    html = textwrap.dedent("""
            <!DOCTYPE html>
            <html>
            <head>
            <style>
            body{background-color:gray}
            div{position:relative;background-color:white;margin:1em auto}
            p{position:absolute;margin:0}
            img{position:absolute}
            </style>
            </head>
            <body>
            """)

    xml = textwrap.dedent("""
            <?xml version="1.0"?>
            <document name="%s">
            """
            % filename
            )

    xhtml = textwrap.dedent("""
            <?xml version="1.0"?>
            <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
            <html xmlns="http://www.w3.org/1999/xhtml">
            <head>
            <style>
            body{background-color:gray}
            div{background-color:white;margin:1em;padding:1em}
            p{white-space:pre-wrap}
            </style>
            </head>
            <body>
            """)

    text = ""
    json = '{"document": "%s", "pages": [\n' % filename
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
