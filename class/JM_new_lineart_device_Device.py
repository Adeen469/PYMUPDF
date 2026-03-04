"""
Class: fitz.JM_new_lineart_device_Device

Description:
LINEART device for Python method Page.get_cdrawings()

Inheritance (MRO): JM_new_lineart_device_Device -> FzDevice2 -> FzDevice -> object

"""

import fitz

# ===== Methods and Attributes of fitz.JM_new_lineart_device_Device =====

# __bool__(self)  [function]

# __eq__(self, value, /)  [wrapper_descriptor]
#     -> Return self==value.

# __gt__(self, value, /)  [wrapper_descriptor]
#     -> Return self>value.

# __hash__(self, /)  [wrapper_descriptor]
#     -> Return hash(self).

# __init__(self, out, clips, method)  [function]
#     -> == Constructor.

# __lt__(self, value, /)  [wrapper_descriptor]
#     -> Return self<value.

# __ne__(self, value, /)  [wrapper_descriptor]
#     -> Return self!=value.

# __repr__(self)  [function]

# __str__(self, /)  [wrapper_descriptor]
#     -> Return str(self).

# begin_group(dev, ctx, bbox, cs, isolated, knockout, blendmode, alpha)  [function]

# begin_layer(dev, ctx, name)  [function]

# begin_mask(self, arg_0, arg_2, arg_3, arg_4, arg_5, arg_6)  [function]

# begin_metatext(self, arg_0, arg_2, arg_3)  [function]

# begin_structure(self, arg_0, arg_2, arg_3, arg_4)  [function]

# begin_tile(self, arg_0, arg_2, arg_3, arg_4, arg_5, arg_6, arg_7, arg_8)  [function]

# clip_image_mask(dev, ctx, image, ctm, scissor)  [function]

# clip_path(dev, ctx, path, even_odd, ctm, scissor)  [function]

# clip_stroke_path(dev, ctx, path, stroke, ctm, scissor)  [function]

# clip_stroke_text(dev, ctx, text, stroke, ctm, scissor)  [function]

# clip_text(dev, ctx, text, ctm, scissor)  [function]

# close_device(self, arg_0)  [function]
#     -> Default virtual method implementations; these all throw an exception.

# drop_device(self, arg_0)  [function]

# end_group(dev, ctx)  [function]

# end_layer(dev, ctx)  [function]

# end_mask(self, arg_0, arg_2)  [function]

# end_metatext(self, arg_0)  [function]

# end_structure(self, arg_0)  [function]

# end_tile(self, arg_0)  [function]

# fill_image(dev, ctx, *vargs)  [function]

# fill_image_mask(dev, ctx, *vargs)  [function]

# fill_path(dev, ctx, path, even_odd, ctm, colorspace, color, alpha, color_params)  [function]

# fill_shade(dev, ctx, *vargs)  [function]

# fill_text(dev, ctx, *vargs)  [function]

# fz_begin_group(self, area, cs, isolated, knockout, blendmode, alpha)  [function]
#     -> Class-aware wrapper for `::fz_begin_group()`.

# fz_begin_layer(self, layer_name)  [function]
#     -> Class-aware wrapper for `::fz_begin_layer()`.

# fz_begin_mask(self, area, luminosity, colorspace, bc, color_params)  [function]
#     -> Class-aware wrapper for `::fz_begin_mask()`.

# fz_begin_metatext(self, meta, text)  [function]
#     -> Class-aware wrapper for `::fz_begin_metatext()`.

# fz_begin_structure(self, standard, raw, idx)  [function]
#     -> Class-aware wrapper for `::fz_begin_structure()`.

# fz_begin_tile(self, area, view, xstep, ystep, ctm)  [function]
#     -> Class-aware wrapper for `::fz_begin_tile()`.

# fz_begin_tile_id(self, area, view, xstep, ystep, ctm, id)  [function]
#     -> Class-aware wrapper for `::fz_begin_tile_id()`.

# fz_begin_tile_tid(self, area, view, xstep, ystep, ctm, id, doc_id)  [function]
#     -> Class-aware wrapper for `::fz_begin_tile_tid()`.

# fz_clip_image_mask(self, image, ctm, scissor)  [function]
#     -> Class-aware wrapper for `::fz_clip_image_mask()`.

# fz_clip_path(self, path, even_odd, ctm, scissor)  [function]
#     -> Class-aware wrapper for `::fz_clip_path()`.

# fz_clip_stroke_path(self, path, stroke, ctm, scissor)  [function]
#     -> Class-aware wrapper for `::fz_clip_stroke_path()`.

# fz_clip_stroke_text(self, text, stroke, ctm, scissor)  [function]
#     -> Class-aware wrapper for `::fz_clip_stroke_text()`.

# fz_clip_text(self, text, ctm, scissor)  [function]
#     -> Class-aware wrapper for `::fz_clip_text()`.

# fz_close_device(self)  [function]
#     -> Class-aware wrapper for `::fz_close_device()`.

# fz_device_current_scissor(self)  [function]
#     -> Class-aware wrapper for `::fz_device_current_scissor()`.

# fz_disable_device_hints(self, hints)  [function]
#     -> Class-aware wrapper for `::fz_disable_device_hints()`.

# fz_enable_device_hints(self, hints)  [function]
#     -> Class-aware wrapper for `::fz_enable_device_hints()`.

# fz_end_group(self)  [function]
#     -> Class-aware wrapper for `::fz_end_group()`.

# fz_end_layer(self)  [function]
#     -> Class-aware wrapper for `::fz_end_layer()`.

# fz_end_mask(self)  [function]
#     -> Class-aware wrapper for `::fz_end_mask()`.

# fz_end_mask_tr(self, fn)  [function]
#     -> Class-aware wrapper for `::fz_end_mask_tr()`.

# fz_end_metatext(self)  [function]
#     -> Class-aware wrapper for `::fz_end_metatext()`.

# fz_end_structure(self)  [function]
#     -> Class-aware wrapper for `::fz_end_structure()`.

# fz_end_tile(self)  [function]
#     -> Class-aware wrapper for `::fz_end_tile()`.

# fz_fill_image(self, image, ctm, alpha, color_params)  [function]
#     -> Class-aware wrapper for `::fz_fill_image()`.

# fz_fill_image_mask(self, image, ctm, colorspace, color, alpha, color_params)  [function]
#     -> Class-aware wrapper for `::fz_fill_image_mask()`.

# fz_fill_path(self, path, even_odd, ctm, colorspace, color, alpha, color_params)  [function]
#     -> Class-aware wrapper for `::fz_fill_path()`.

# fz_fill_shade(self, shade, ctm, alpha, color_params)  [function]
#     -> Class-aware wrapper for `::fz_fill_shade()`.

# fz_fill_text(dev, text, ctm, colorspace, color, alpha, color_params)  [function]
#     -> Python version of fz_fill_text() taking list/tuple for `color`.

# fz_ignore_text(self, text, ctm)  [function]
#     -> Class-aware wrapper for `::fz_ignore_text()`.

# fz_new_draw_device_type3(transform, dest)  [function]
#     -> Class-aware wrapper for `::fz_new_draw_device_type3()`.

# fz_new_ocr_device(self, ctm, mediabox, with_list, language, datadir, progress, progress_arg)  [function]
#     -> Class-aware wrapper for `::fz_new_ocr_device()`.

# fz_new_ocr_device_with_options(self, ctm, mediabox, with_list, language, datadir, progress, progress_arg, options)  [function]
#     -> Class-aware wrapper for `::fz_new_ocr_device_with_options()`.

# fz_new_xmltext_device(out)  [function]
#     -> Class-aware wrapper for `::fz_new_xmltext_device()`.

# fz_pop_clip(self)  [function]
#     -> Class-aware wrapper for `::fz_pop_clip()`.

# fz_render_flags(self, set, clear)  [function]
#     -> Class-aware wrapper for `::fz_render_flags()`.

# fz_render_t3_glyph_direct(self, font, gid, trm, gstate, def_cs, fill_gstate, stroke_gstate)  [function]
#     -> Class-aware wrapper for `::fz_render_t3_glyph_direct()`.

# fz_set_default_colorspaces(self, default_cs)  [function]
#     -> Class-aware wrapper for `::fz_set_default_colorspaces()`.

# fz_stroke_path(self, path, stroke, ctm, colorspace, color, alpha, color_params)  [function]
#     -> Class-aware wrapper for `::fz_stroke_path()`.

# fz_stroke_text(self, text, stroke, ctm, colorspace, color, alpha, color_params)  [function]
#     -> Class-aware wrapper for `::fz_stroke_text()`.

# ignore_text(dev, ctx, *vargs)  [function]

# m_internal = <property object at 0x000002052DC5E5C0>  [property]

# m_internal_value(self)  [function]
#     -> Return numerical value of .m_internal; helps with Python debugging.

# pop_clip(dev, ctx)  [function]

# render_flags(self, arg_0, arg_2, arg_3)  [function]

# s_num_instances = <property object at 0x000002052DC5E610>  [property]

# set_default_colorspaces(self, arg_0, arg_2)  [function]

# stroke_path(dev, ctx, path, stroke, ctm, colorspace, color, alpha, color_params)  [function]

# stroke_text(dev, ctx, *vargs)  [function]

# thisown = <property object at 0x000002052DC5E6B0>  [property]

# use_virtual_begin_group(self, use=True)  [function]

# use_virtual_begin_layer(self, use=True)  [function]

# use_virtual_begin_mask(self, use=True)  [function]

# use_virtual_begin_metatext(self, use=True)  [function]

# use_virtual_begin_structure(self, use=True)  [function]

# use_virtual_begin_tile(self, use=True)  [function]

# use_virtual_clip_image_mask(self, use=True)  [function]

# use_virtual_clip_path(self, use=True)  [function]

# use_virtual_clip_stroke_path(self, use=True)  [function]

# use_virtual_clip_stroke_text(self, use=True)  [function]

# use_virtual_clip_text(self, use=True)  [function]

# use_virtual_close_device(self, use=True)  [function]
#     -> These methods set the function pointers in *m_internal

# use_virtual_drop_device(self, use=True)  [function]

# use_virtual_end_group(self, use=True)  [function]

# use_virtual_end_layer(self, use=True)  [function]

# use_virtual_end_mask(self, use=True)  [function]

# use_virtual_end_metatext(self, use=True)  [function]

# use_virtual_end_structure(self, use=True)  [function]

# use_virtual_end_tile(self, use=True)  [function]

# use_virtual_fill_image(self, use=True)  [function]

# use_virtual_fill_image_mask(self, use=True)  [function]

# use_virtual_fill_path(self, use=True)  [function]

# use_virtual_fill_shade(self, use=True)  [function]

# use_virtual_fill_text(self, use=True)  [function]

# use_virtual_ignore_text(self, use=True)  [function]

# use_virtual_pop_clip(self, use=True)  [function]

# use_virtual_render_flags(self, use=True)  [function]

# use_virtual_set_default_colorspaces(self, use=True)  [function]

# use_virtual_stroke_path(self, use=True)  [function]

# use_virtual_stroke_text(self, use=True)  [function]


# ===== Source Code =====
class JM_new_lineart_device_Device(mupdf.FzDevice2):
    '''
    LINEART device for Python method Page.get_cdrawings()
    '''
    #log(f'JM_new_lineart_device_Device()')
    def __init__(self, out, clips, method):
        #log(f'JM_new_lineart_device_Device.__init__()')
        super().__init__()
        # fixme: this results in "Unexpected call of unimplemented virtual_fnptrs fn FzDevice2::drop_device().".
        #self.use_virtual_drop_device()
        self.use_virtual_fill_path()
        self.use_virtual_stroke_path()
        self.use_virtual_clip_path()
        self.use_virtual_clip_image_mask()
        self.use_virtual_clip_stroke_path()
        self.use_virtual_clip_stroke_text()
        self.use_virtual_clip_text()
        
        self.use_virtual_fill_text
        self.use_virtual_stroke_text
        self.use_virtual_ignore_text
        
        self.use_virtual_fill_shade()
        self.use_virtual_fill_image()
        self.use_virtual_fill_image_mask()
        
        self.use_virtual_pop_clip()
        
        self.use_virtual_begin_group()
        self.use_virtual_end_group()
        
        self.use_virtual_begin_layer()
        self.use_virtual_end_layer()
        
        self.out = out
        self.seqno = 0
        self.depth = 0
        self.clips = clips
        self.method = method
        
        self.scissors = None
        self.layer_name = ""  # optional content name
        self.pathrect = None
        
        self.linewidth = 0
        self.ptm = mupdf.FzMatrix()
        self.ctm = mupdf.FzMatrix()
        self.rot = mupdf.FzMatrix()
        self.lastpoint = mupdf.FzPoint()
        self.firstpoint = mupdf.FzPoint()
        self.havemove = 0
        self.pathrect = mupdf.FzRect()
        self.pathfactor = 0
        self.linecount = 0
        self.path_type = 0
    
    #drop_device = jm_lineart_drop_device
    
    fill_path           = jm_lineart_fill_path
    stroke_path         = jm_lineart_stroke_path
    clip_image_mask     = jm_lineart_clip_image_mask
    clip_path           = jm_lineart_clip_path
    clip_stroke_path    = jm_lineart_clip_stroke_path
    clip_text           = jm_lineart_clip_text
    clip_stroke_text    = jm_lineart_clip_stroke_text
    
    fill_text           = jm_increase_seqno
    stroke_text         = jm_increase_seqno
    ignore_text         = jm_increase_seqno
    
    fill_shade          = jm_increase_seqno
    fill_image          = jm_increase_seqno
    fill_image_mask     = jm_increase_seqno
    
    pop_clip            = jm_lineart_pop_clip
    
    begin_group         = jm_lineart_begin_group
    end_group           = jm_lineart_end_group
    
    begin_layer         = jm_lineart_begin_layer
    end_layer           = jm_lineart_end_layer
