"""
Class: fitz.Outline

Description: No docstring available.

Inheritance (MRO): Outline -> object

"""

import fitz

# ===== Methods and Attributes of fitz.Outline =====

# __eq__(self, value, /)  [wrapper_descriptor]
#     -> Return self==value.

# __gt__(self, value, /)  [wrapper_descriptor]
#     -> Return self>value.

# __hash__(self, /)  [wrapper_descriptor]
#     -> Return hash(self).

# __init__(self, ol)  [function]
#     -> Initialize self.  See help(type(self)) for accurate signature.

# __lt__(self, value, /)  [wrapper_descriptor]
#     -> Return self<value.

# __ne__(self, value, /)  [wrapper_descriptor]
#     -> Return self!=value.

# __repr__(self, /)  [wrapper_descriptor]
#     -> Return repr(self).

# __str__(self, /)  [wrapper_descriptor]
#     -> Return str(self).

# dest = <property object at 0x000002052DE32700>  [property]

# destination(self, document)  [function]
#     -> Like `dest` property but uses `document` to resolve destinations for

# down = <property object at 0x000002052DE32660>  [property]

# is_external = <property object at 0x000002052DE326B0>  [property]

# is_open = <property object at 0x000002052DE32750>  [property]

# next = <property object at 0x000002052DE327A0>  [property]

# page = <property object at 0x000002052DE327F0>  [property]

# this = <member 'this' of 'Outline' objects>  [member_descriptor]

# title = <property object at 0x000002052DE32840>  [property]

# uri = <property object at 0x000002052DE32890>  [property]

# x = <property object at 0x000002052DE328E0>  [property]

# y = <property object at 0x000002052DE32930>  [property]


# ===== Source Code =====
class Outline:

    def __init__(self, ol):
        self.this = ol

    @property
    def dest(self):
        '''outline destination details'''
        return linkDest(self, None, None)

    def destination(self, document):
        '''
        Like `dest` property but uses `document` to resolve destinations for
        kind=LINK_NAMED.
        '''
        return linkDest(self, None, document)
        
    @property
    def down(self):
        ol = self.this
        down_ol = ol.down()
        if not down_ol.m_internal:
            return
        return Outline(down_ol)

    @property
    def is_external(self):
        if g_use_extra:
            # calling _extra.* here appears to save significant time in
            # test_toc.py:test_full_toc, 1.2s=>0.94s.
            #
            return _extra.Outline_is_external( self.this)
        ol = self.this
        if not ol.m_internal:
            return False
        uri = ol.m_internal.uri if 1 else ol.uri()
        if uri is None:
            return False
        return mupdf.fz_is_external_link(uri)

    @property
    def is_open(self):
        if 1:
            return self.this.m_internal.is_open
        return self.this.is_open()

    @property
    def next(self):
        ol = self.this
        next_ol = ol.next()
        if not next_ol.m_internal:
            return
        return Outline(next_ol)

    @property
    def page(self):
        if 1:
            return self.this.m_internal.page.page
        return self.this.page().page

    @property
    def title(self):
        return self.this.m_internal.title

    @property
    def uri(self):
        ol = self.this
        if not ol.m_internal:
            return None
        return ol.m_internal.uri

    @property
    def x(self):
        return self.this.m_internal.x

    @property
    def y(self):
        return self.this.m_internal.y

    __slots__ = [ 'this']
