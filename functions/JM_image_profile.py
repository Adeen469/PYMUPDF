"""
Function: fitz.JM_image_profile
Signature: JM_image_profile(imagedata, keep_image)
Description:
Return basic properties of an image provided as bytes or bytearray
The function creates an fz_image and optionally returns it.
"""

import fitz

# Source code of fitz.JM_image_profile:
def JM_image_profile( imagedata, keep_image):
    '''
    Return basic properties of an image provided as bytes or bytearray
    The function creates an fz_image and optionally returns it.
    '''
    if not imagedata:
        return None # nothing given
    
    len_ = len( imagedata)
    if len_ < 8:
        message( "bad image data")
        return None
    c = imagedata
    #log( 'calling mfz_recognize_image_format with {c!r=}')
    type_ = mupdf.fz_recognize_image_format( c)
    if type_ == mupdf.FZ_IMAGE_UNKNOWN:
        return None

    if keep_image:
        res = mupdf.fz_new_buffer_from_copied_data( c, len_)
    else:
        res = mupdf.fz_new_buffer_from_shared_data( c, len_)
    image = mupdf.fz_new_image_from_buffer( res)
    ctm = mupdf.fz_image_orientation_matrix( image)
    xres, yres = mupdf.fz_image_resolution(image)
    orientation = mupdf.fz_image_orientation( image)
    cs_name = mupdf.fz_colorspace_name( image.colorspace())
    result = dict()
    result[ dictkey_width] = image.w()
    result[ dictkey_height] = image.h()
    result[ "orientation"] = orientation
    result[ dictkey_matrix] = JM_py_from_matrix(ctm)
    result[ dictkey_xres] = xres
    result[ dictkey_yres] = yres
    result[ dictkey_colorspace] = image.n()
    result[ dictkey_bpc] = image.bpc()
    result[ dictkey_ext] = JM_image_extension(type_)
    result[ dictkey_cs_name] = cs_name

    if keep_image:
        result[ dictkey_image] = image
    return result
