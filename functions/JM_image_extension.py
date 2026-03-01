"""
Function: fitz.JM_image_extension
Signature: JM_image_extension(type_)
Description:
return extension for MuPDF image type
"""

import fitz

# Source code of fitz.JM_image_extension:
def JM_image_extension(type_):
    '''
    return extension for MuPDF image type
    '''
    if type_ == mupdf.FZ_IMAGE_FAX:     return "fax"
    if type_ == mupdf.FZ_IMAGE_RAW:     return "raw"
    if type_ == mupdf.FZ_IMAGE_FLATE:   return "flate"
    if type_ == mupdf.FZ_IMAGE_LZW:     return "lzw"
    if type_ == mupdf.FZ_IMAGE_RLD:     return "rld"
    if type_ == mupdf.FZ_IMAGE_BMP:     return "bmp"
    if type_ == mupdf.FZ_IMAGE_GIF:     return "gif"
    if type_ == mupdf.FZ_IMAGE_JBIG2:   return "jb2"
    if type_ == mupdf.FZ_IMAGE_JPEG:    return "jpeg"
    if type_ == mupdf.FZ_IMAGE_JPX:     return "jpx"
    if type_ == mupdf.FZ_IMAGE_JXR:     return "jxr"
    if type_ == mupdf.FZ_IMAGE_PNG:     return "png"
    if type_ == mupdf.FZ_IMAGE_PNM:     return "pnm"
    if type_ == mupdf.FZ_IMAGE_TIFF:    return "tiff"
    #if type_ == mupdf.FZ_IMAGE_PSD:     return "psd"
    return "n/a"
