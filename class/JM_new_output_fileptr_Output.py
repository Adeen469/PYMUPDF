"""
Class: fitz.JM_new_output_fileptr_Output

Description:
Wrapper class for struct fz_output with virtual fns for each fnptr; this is for use as a SWIG Director class.

Inheritance (MRO): JM_new_output_fileptr_Output -> FzOutput2 -> FzOutput -> object

"""

import fitz

# ===== Methods and Attributes of fitz.JM_new_output_fileptr_Output =====

# Filter_85 = 1  [int]

# Filter_HEX = 0  [int]

# Filter_RLE = 2  [int]

# Fixed_STDERR = 2  [int]

# Fixed_STDOUT = 1  [int]

# __bool__(self)  [function]

# __eq__(self, value, /)  [wrapper_descriptor]
#     -> Return self==value.

# __gt__(self, value, /)  [wrapper_descriptor]
#     -> Return self>value.

# __hash__(self, /)  [wrapper_descriptor]
#     -> Return hash(self).

# __init__(self, bio)  [function]
#     -> == Constructor.

# __lt__(self, value, /)  [wrapper_descriptor]
#     -> Return self<value.

# __ne__(self, value, /)  [wrapper_descriptor]
#     -> Return self!=value.

# __repr__(self)  [function]

# __str__(self, /)  [wrapper_descriptor]
#     -> Return str(self).

# as_stream(self, arg_0)  [function]

# close(self, arg_0)  [function]

# drop(self, arg_0)  [function]

# fz_close_output(self)  [function]
#     -> Class-aware wrapper for `::fz_close_output()`.

# fz_debug_store(self)  [function]
#     -> Class-aware wrapper for `::fz_debug_store()`.

# fz_dump_glyph_cache_stats(self)  [function]
#     -> Class-aware wrapper for `::fz_dump_glyph_cache_stats()`.

# fz_flush_output(self)  [function]
#     -> Class-aware wrapper for `::fz_flush_output()`.

# fz_int2_heap_dump(self, heap)  [function]
#     -> Class-aware wrapper for `::fz_int2_heap_dump()`.

# fz_int_heap_dump(self, heap)  [function]
#     -> Class-aware wrapper for `::fz_int_heap_dump()`.

# fz_intptr_heap_dump(self, heap)  [function]
#     -> Class-aware wrapper for `::fz_intptr_heap_dump()`.

# fz_new_svg_device(self, page_width, page_height, text_format, reuse_images)  [function]
#     -> Class-aware wrapper for `::fz_new_svg_device()`.

# fz_new_svg_device_with_id(self, page_width, page_height, text_format, reuse_images)  [function]
#     -> Helper for out-params of class method fz_output::ll_fz_new_svg_device_with_id() [fz_new_svg_device_with_id()].

# fz_new_svg_device_with_options(self, page_width, page_height, opts)  [function]
#     -> Class-aware wrapper for `::fz_new_svg_device_with_options()`.

# fz_new_trace_device(self)  [function]
#     -> Class-aware wrapper for `::fz_new_trace_device()`.

# fz_new_xmltext_device(self)  [function]
#     -> Class-aware wrapper for `::fz_new_xmltext_device()`.

# fz_output_supports_stream(self)  [function]
#     -> Class-aware wrapper for `::fz_output_supports_stream()`.

# fz_output_xml(self, item, level)  [function]
#     -> Class-aware wrapper for `::fz_output_xml()`.

# fz_print_stext_header_as_html(self)  [function]
#     -> Class-aware wrapper for `::fz_print_stext_header_as_html()`.

# fz_print_stext_header_as_xhtml(self)  [function]
#     -> Class-aware wrapper for `::fz_print_stext_header_as_xhtml()`.

# fz_print_stext_page_as_html(self, page, id)  [function]
#     -> Class-aware wrapper for `::fz_print_stext_page_as_html()`.

# fz_print_stext_page_as_json(self, page, scale)  [function]
#     -> Class-aware wrapper for `::fz_print_stext_page_as_json()`.

# fz_print_stext_page_as_text(self, page)  [function]
#     -> Class-aware wrapper for `::fz_print_stext_page_as_text()`.

# fz_print_stext_page_as_xhtml(self, page, id)  [function]
#     -> Class-aware wrapper for `::fz_print_stext_page_as_xhtml()`.

# fz_print_stext_page_as_xml(self, page, id)  [function]
#     -> Class-aware wrapper for `::fz_print_stext_page_as_xml()`.

# fz_print_stext_trailer_as_html(self)  [function]
#     -> Class-aware wrapper for `::fz_print_stext_trailer_as_html()`.

# fz_print_stext_trailer_as_xhtml(self)  [function]
#     -> Class-aware wrapper for `::fz_print_stext_trailer_as_xhtml()`.

# fz_reset_output(self)  [function]
#     -> Class-aware wrapper for `::fz_reset_output()`.

# fz_seek_output(self, off, whence)  [function]
#     -> Class-aware wrapper for `::fz_seek_output()`.

# fz_set_stddbg(self)  [function]
#     -> Class-aware wrapper for `::fz_set_stddbg()`.

# fz_stream_from_output(self)  [function]
#     -> Class-aware wrapper for `::fz_stream_from_output()`.

# fz_tell_output(self)  [function]
#     -> Class-aware wrapper for `::fz_tell_output()`.

# fz_truncate_output(self)  [function]
#     -> Class-aware wrapper for `::fz_truncate_output()`.

# fz_write_base64(self, data, size, newline)  [function]
#     -> Class-aware wrapper for `::fz_write_base64()`.

# fz_write_base64_buffer(self, data, newline)  [function]
#     -> Class-aware wrapper for `::fz_write_base64_buffer()`.

# fz_write_bitmap_as_pbm(self, bitmap)  [function]
#     -> Class-aware wrapper for `::fz_write_bitmap_as_pbm()`.

# fz_write_bitmap_as_pcl(self, bitmap, pcl)  [function]
#     -> Class-aware wrapper for `::fz_write_bitmap_as_pcl()`.

# fz_write_bitmap_as_pkm(self, bitmap)  [function]
#     -> Class-aware wrapper for `::fz_write_bitmap_as_pkm()`.

# fz_write_bitmap_as_pwg(self, bitmap, pwg)  [function]
#     -> Class-aware wrapper for `::fz_write_bitmap_as_pwg()`.

# fz_write_bitmap_as_pwg_page(self, bitmap, pwg)  [function]
#     -> Class-aware wrapper for `::fz_write_bitmap_as_pwg_page()`.

# fz_write_bits(self, data, num_bits)  [function]
#     -> Class-aware wrapper for `::fz_write_bits()`.

# fz_write_bits_sync(self)  [function]
#     -> Class-aware wrapper for `::fz_write_bits_sync()`.

# fz_write_buffer(self, data)  [function]
#     -> Class-aware wrapper for `::fz_write_buffer()`.

# fz_write_byte(self, x)  [function]
#     -> Class-aware wrapper for `::fz_write_byte()`.

# fz_write_char(self, x)  [function]
#     -> Class-aware wrapper for `::fz_write_char()`.

# fz_write_data(self, data, size)  [function]
#     -> Class-aware wrapper for `::fz_write_data()`.

# fz_write_float_be(self, f)  [function]
#     -> Class-aware wrapper for `::fz_write_float_be()`.

# fz_write_float_le(self, f)  [function]
#     -> Class-aware wrapper for `::fz_write_float_le()`.

# fz_write_image_as_data_uri(self, image)  [function]
#     -> Class-aware wrapper for `::fz_write_image_as_data_uri()`.

# fz_write_int16_be(self, x)  [function]
#     -> Class-aware wrapper for `::fz_write_int16_be()`.

# fz_write_int16_le(self, x)  [function]
#     -> Class-aware wrapper for `::fz_write_int16_le()`.

# fz_write_int32_be(self, x)  [function]
#     -> Class-aware wrapper for `::fz_write_int32_be()`.

# fz_write_int32_le(self, x)  [function]
#     -> Class-aware wrapper for `::fz_write_int32_le()`.

# fz_write_json(self, value)  [function]
#     -> Class-aware wrapper for `::fz_write_json()`.

# fz_write_pixmap_as_data_uri(self, pixmap)  [function]
#     -> Class-aware wrapper for `::fz_write_pixmap_as_data_uri()`.

# fz_write_pixmap_as_jpeg(self, pix, quality, invert_cmyk)  [function]
#     -> Class-aware wrapper for `::fz_write_pixmap_as_jpeg()`.

# fz_write_pixmap_as_jpx(self, pix, quality)  [function]
#     -> Class-aware wrapper for `::fz_write_pixmap_as_jpx()`.

# fz_write_pixmap_as_pam(self, pixmap)  [function]
#     -> Class-aware wrapper for `::fz_write_pixmap_as_pam()`.

# fz_write_pixmap_as_pbm(self, pixmap)  [function]
#     -> Class-aware wrapper for `::fz_write_pixmap_as_pbm()`.

# fz_write_pixmap_as_pcl(self, pixmap, pcl)  [function]
#     -> Class-aware wrapper for `::fz_write_pixmap_as_pcl()`.

# fz_write_pixmap_as_pclm(self, pixmap, options)  [function]
#     -> Class-aware wrapper for `::fz_write_pixmap_as_pclm()`.

# fz_write_pixmap_as_pdfocr(self, pixmap, options)  [function]
#     -> Class-aware wrapper for `::fz_write_pixmap_as_pdfocr()`.

# fz_write_pixmap_as_pkm(self, pixmap)  [function]
#     -> Class-aware wrapper for `::fz_write_pixmap_as_pkm()`.

# fz_write_pixmap_as_png(self, pixmap)  [function]
#     -> Class-aware wrapper for `::fz_write_pixmap_as_png()`.

# fz_write_pixmap_as_pnm(self, pixmap)  [function]
#     -> Class-aware wrapper for `::fz_write_pixmap_as_pnm()`.

# fz_write_pixmap_as_ps(self, pixmap)  [function]
#     -> Class-aware wrapper for `::fz_write_pixmap_as_ps()`.

# fz_write_pixmap_as_psd(self, pixmap)  [function]
#     -> Class-aware wrapper for `::fz_write_pixmap_as_psd()`.

# fz_write_pixmap_as_pwg(self, pixmap, pwg)  [function]
#     -> Class-aware wrapper for `::fz_write_pixmap_as_pwg()`.

# fz_write_pixmap_as_pwg_page(self, pixmap, pwg)  [function]
#     -> Class-aware wrapper for `::fz_write_pixmap_as_pwg_page()`.

# fz_write_ps_file_header(self)  [function]
#     -> Class-aware wrapper for `::fz_write_ps_file_header()`.

# fz_write_ps_file_trailer(self, pages)  [function]
#     -> Class-aware wrapper for `::fz_write_ps_file_trailer()`.

# fz_write_pwg_file_header(self)  [function]
#     -> Class-aware wrapper for `::fz_write_pwg_file_header()`.

# fz_write_rune(self, rune)  [function]
#     -> Class-aware wrapper for `::fz_write_rune()`.

# fz_write_stream(self, _in)  [function]
#     -> Class-aware wrapper for `::fz_write_stream()`.

# fz_write_string(self, s)  [function]
#     -> Class-aware wrapper for `::fz_write_string()`.

# fz_write_uint16_be(self, x)  [function]
#     -> Class-aware wrapper for `::fz_write_uint16_be()`.

# fz_write_uint16_le(self, x)  [function]
#     -> Class-aware wrapper for `::fz_write_uint16_le()`.

# fz_write_uint32_be(self, x)  [function]
#     -> Class-aware wrapper for `::fz_write_uint32_be()`.

# fz_write_uint32_le(self, x)  [function]
#     -> Class-aware wrapper for `::fz_write_uint32_le()`.

# m_internal = <property object at 0x000002052DCDB330>  [property]

# m_internal_value(self)  [function]
#     -> Return numerical value of .m_internal; helps with Python debugging.

# pdf_new_output_processor(self, ahxencode, newlines)  [function]
#     -> Class-aware wrapper for `::pdf_new_output_processor()`.

# pdf_print_crypt(self, crypt)  [function]
#     -> Class-aware wrapper for `::pdf_print_crypt()`.

# pdf_print_encrypted_obj(self, obj, tight, ascii, crypt, num, gen)  [function]
#     -> Helper for out-params of class method fz_output::ll_pdf_print_encrypted_obj() [pdf_print_encrypted_obj()].

# pdf_print_font(self, fontdesc)  [function]
#     -> Class-aware wrapper for `::pdf_print_font()`.

# pdf_print_obj(self, obj, tight, ascii)  [function]
#     -> Class-aware wrapper for `::pdf_print_obj()`.

# pdf_write_digest(self, byte_range, field, digest_offset, digest_length, signer)  [function]
#     -> Class-aware wrapper for `::pdf_write_digest()`.

# reset(self, arg_0)  [function]

# s_num_instances = <property object at 0x000002052DCDB380>  [property]

# seek(self, ctx, offset, whence)  [function]

# tell(self, ctx)  [function]

# thisown = <property object at 0x000002052DCDB470>  [property]

# truncate(self, ctx)  [function]

# use_virtual_as_stream(self, use=True)  [function]

# use_virtual_close(self, use=True)  [function]

# use_virtual_drop(self, use=True)  [function]

# use_virtual_reset(self, use=True)  [function]

# use_virtual_seek(self, use=True)  [function]

# use_virtual_tell(self, use=True)  [function]

# use_virtual_truncate(self, use=True)  [function]

# use_virtual_write(self, use=True)  [function]
#     -> These methods set the function pointers in *m_internal

# write(self, ctx, data_raw, data_length)  [function]
#     -> Default virtual method implementations; these all throw an exception.


# ===== Source Code =====
class JM_new_output_fileptr_Output(mupdf.FzOutput2):
    def __init__(self, bio):
        super().__init__()
        self.bio = bio
        self.use_virtual_write()
        self.use_virtual_seek()
        self.use_virtual_tell()
        self.use_virtual_truncate()
    
    def seek( self, ctx, offset, whence):
        return self.bio.seek( offset, whence)
    
    def tell( self, ctx):
        ret = self.bio.tell()
        return ret
    
    def truncate( self, ctx):
        return self.bio.truncate()
    
    def write(self, ctx, data_raw, data_length):
        data = mupdf.raw_to_python_bytes(data_raw, data_length)
        return self.bio.write(data)
