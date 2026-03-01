"""
Function: fitz.JM_append_word
Signature: JM_append_word(lines, buff, wbbox, block_n, line_n, word_n)
Description:
Functions for wordlist output
"""

import fitz

# Source code of fitz.JM_append_word:
def JM_append_word(lines, buff, wbbox, block_n, line_n, word_n):
    '''
    Functions for wordlist output
    '''
    s = JM_EscapeStrFromBuffer(buff)
    litem = (
            wbbox.x0,
            wbbox.y0,
            wbbox.x1,
            wbbox.y1,
            s,
            block_n,
            line_n,
            word_n,
            )
    lines.append(litem)
    return word_n + 1, mupdf.FzRect(mupdf.FzRect.Fixed_EMPTY)   # word counter
