"""
Function: fitz.get_pdf_now
Signature: get_pdf_now() -> str
Description:
"Now" timestamp in PDF Format
"""

import fitz

# Source code of fitz.get_pdf_now:
def get_pdf_now() -> str:
    '''
    "Now" timestamp in PDF Format
    '''
    import time
    tz = "%s'%s'" % (
        str(abs(time.altzone // 3600)).rjust(2, "0"),
        str((abs(time.altzone // 60) % 60)).rjust(2, "0"),
    )
    tstamp = time.strftime("D:%Y%m%d%H%M%S", time.localtime())
    if time.altzone > 0:
        tstamp += "-" + tz
    elif time.altzone < 0:
        tstamp += "+" + tz
    else:
        pass
    return tstamp
