"""
Class: fitz.Walker

Description:
Wrapper class for struct fz_path_walker with virtual fns for each fnptr; this is for use as a SWIG Director class.

Inheritance (MRO): Walker -> FzPathWalker2 -> FzPathWalker -> object

"""

import fitz

# ===== Methods and Attributes of fitz.Walker =====

# __bool__(self)  [function]

# __eq__(self, value, /)  [wrapper_descriptor]
#     -> Return self==value.

# __gt__(self, value, /)  [wrapper_descriptor]
#     -> Return self>value.

# __hash__(self, /)  [wrapper_descriptor]
#     -> Return hash(self).

# __init__(self, dev)  [function]
#     -> == Constructor.

# __lt__(self, value, /)  [wrapper_descriptor]
#     -> Return self<value.

# __ne__(self, value, /)  [wrapper_descriptor]
#     -> Return self!=value.

# __repr__(self)  [function]

# __str__(self, /)  [wrapper_descriptor]
#     -> Return str(self).

# closepath(self, ctx)  [function]

# curveto(self, ctx, x1, y1, x2, y2, x3, y3)  [function]

# curvetov(self, arg_0, arg_2, arg_3, arg_4, arg_5)  [function]

# curvetoy(self, arg_0, arg_2, arg_3, arg_4, arg_5)  [function]

# lineto(self, ctx, x, y)  [function]

# m_internal = <property object at 0x000002052DCDB920>  [property]

# m_internal_value(self)  [function]
#     -> Return numerical value of .m_internal; helps with Python debugging.

# moveto(self, ctx, x, y)  [function]
#     -> Default virtual method implementations; these all throw an exception.

# quadto(self, arg_0, arg_2, arg_3, arg_4, arg_5)  [function]

# rectto(self, arg_0, arg_2, arg_3, arg_4, arg_5)  [function]

# s_num_instances = <property object at 0x000002052DCDB970>  [property]

# thisown = <property object at 0x000002052DCDBA60>  [property]

# use_virtual_closepath(self, use=True)  [function]

# use_virtual_curveto(self, use=True)  [function]

# use_virtual_curvetov(self, use=True)  [function]

# use_virtual_curvetoy(self, use=True)  [function]

# use_virtual_lineto(self, use=True)  [function]

# use_virtual_moveto(self, use=True)  [function]
#     -> These methods set the function pointers in *m_internal

# use_virtual_quadto(self, use=True)  [function]

# use_virtual_rectto(self, use=True)  [function]


# ===== Source Code =====
class Walker(mupdf.FzPathWalker2):

    def __init__(self, dev):
        super().__init__()
        self.use_virtual_moveto()
        self.use_virtual_lineto()
        self.use_virtual_curveto()
        self.use_virtual_closepath()
        self.dev = dev

    def closepath(self, ctx):    # trace_close().
        #log(f'Walker(): {self.dev.pathdict=}')
        try:
            if self.dev.linecount == 3:
                if jm_checkrect(self.dev):
                    #log(f'end1: {self.dev.pathdict=}')
                    return
            self.dev.linecount = 0   # reset # of consec. lines

            if self.dev.havemove:
                if self.dev.lastpoint != self.dev.firstpoint:
                    item = ("l", JM_py_from_point(self.dev.lastpoint),
                                 JM_py_from_point(self.dev.firstpoint))
                    self.dev.pathdict[dictkey_items].append(item)
                    self.dev.lastpoint = self.dev.firstpoint
                self.dev.pathdict["closePath"] = False

            else:
                #log('setting self.dev.pathdict[ "closePath"] to true')
                self.dev.pathdict[ "closePath"] = True
                #log(f'end2: {self.dev.pathdict=}')

            self.dev.havemove = 0

        except Exception:
            if g_exceptions_verbose:    exception_info()
            raise

    def curveto(self, ctx, x1, y1, x2, y2, x3, y3):   # trace_curveto().
        #log(f'Walker(): {self.dev.pathdict=}')
        try:
            self.dev.linecount = 0  # reset # of consec. lines
            p1 = mupdf.fz_make_point(x1, y1)
            p2 = mupdf.fz_make_point(x2, y2)
            p3 = mupdf.fz_make_point(x3, y3)
            p1 = mupdf.fz_transform_point(p1, self.dev.ctm)
            p2 = mupdf.fz_transform_point(p2, self.dev.ctm)
            p3 = mupdf.fz_transform_point(p3, self.dev.ctm)
            self.dev.pathrect = mupdf.fz_include_point_in_rect(self.dev.pathrect, p1)
            self.dev.pathrect = mupdf.fz_include_point_in_rect(self.dev.pathrect, p2)
            self.dev.pathrect = mupdf.fz_include_point_in_rect(self.dev.pathrect, p3)

            list_ = (
                    "c",
                    JM_py_from_point(self.dev.lastpoint),
                    JM_py_from_point(p1),
                    JM_py_from_point(p2),
                    JM_py_from_point(p3),
                    )
            self.dev.lastpoint = p3
            self.dev.pathdict[ dictkey_items].append( list_)
        except Exception:
            if g_exceptions_verbose:    exception_info()
            raise

    def lineto(self, ctx, x, y):   # trace_lineto().
        #log(f'Walker(): {self.dev.pathdict=}')
        try:
            p1 = mupdf.fz_transform_point( mupdf.fz_make_point(x, y), self.dev.ctm)
            self.dev.pathrect = mupdf.fz_include_point_in_rect( self.dev.pathrect, p1)
            list_ = (
                    'l',
                    JM_py_from_point( self.dev.lastpoint),
                    JM_py_from_point(p1),
                    )
            self.dev.lastpoint = p1
            items = self.dev.pathdict[ dictkey_items]
            items.append( list_)
            self.dev.linecount += 1 # counts consecutive lines
            if self.dev.linecount == 4 and self.dev.path_type != trace_device_FILL_PATH:
                # shrink to "re" or "qu" item
                jm_checkquad(self.dev)
        except Exception:
            if g_exceptions_verbose:    exception_info()
            raise

    def moveto(self, ctx, x, y):   # trace_moveto().
        if 0 and isinstance(self.dev.pathdict, dict):
            log(f'self.dev.pathdict:')
            for n, v in self.dev.pathdict.items():
                log( '    {type(n)=} {len(n)=} {n!r} {n}: {v!r}: {v}')

        #log(f'Walker(): {type(self.dev.pathdict)=} {self.dev.pathdict=}')

        try:
            #log( '{=dev.ctm type(dev.ctm)}')
            self.dev.lastpoint = mupdf.fz_transform_point(
                    mupdf.fz_make_point(x, y),
                    self.dev.ctm,
                    )
            if mupdf.fz_is_infinite_rect( self.dev.pathrect):
                self.dev.pathrect = mupdf.fz_make_rect(
                        self.dev.lastpoint.x,
                        self.dev.lastpoint.y,
                        self.dev.lastpoint.x,
                        self.dev.lastpoint.y,
                        )
            self.dev.firstpoint = self.dev.lastpoint
            self.dev.havemove = 1
            self.dev.linecount = 0  # reset # of consec. lines
        except Exception:
            if g_exceptions_verbose:    exception_info()
            raise
