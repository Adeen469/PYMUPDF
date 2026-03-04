"""
Class: fitz.Widget

Description:
Class describing a PDF form field ("widget")

Inheritance (MRO): Widget -> object

"""

import fitz

# ===== Methods and Attributes of fitz.Widget =====

# __eq__(self, value, /)  [wrapper_descriptor]
#     -> Return self==value.

# __gt__(self, value, /)  [wrapper_descriptor]
#     -> Return self>value.

# __hash__(self, /)  [wrapper_descriptor]
#     -> Return hash(self).

# __init__(self)  [function]
#     -> Initialize self.  See help(type(self)) for accurate signature.

# __lt__(self, value, /)  [wrapper_descriptor]
#     -> Return self<value.

# __ne__(self, value, /)  [wrapper_descriptor]
#     -> Return self!=value.

# __repr__(self)  [function]
#     -> Return repr(self).

# __str__(self, /)  [wrapper_descriptor]
#     -> Return str(self).

# button_states(self)  [function]
#     -> Return the on/off state names for button widgets.

# next = <property object at 0x000002052DE325C0>  [property]

# on_state(self)  [function]
#     -> Return the "On" value for button widgets.

# reset(self)  [function]
#     -> Reset the field value to its default.

# update(self, sync_flags=False)  [function]
#     -> Reflect Python object in the PDF.


# ===== Source Code =====
class Widget:
    '''
    Class describing a PDF form field ("widget")
    '''

    def __init__(self):
        self.border_color = None
        self.border_style = "S"
        self.border_width = 0
        self.border_dashes = None
        self.choice_values = None  # choice fields only
        self.rb_parent = None   # radio buttons only: xref of owning parent

        self.field_name = None  # field name
        self.field_label = None # field label
        self.field_value = None
        self.field_flags = 0
        self.field_display = 0
        self.field_type = 0  # valid range 1 through 7
        self.field_type_string = None  # field type as string

        self.fill_color = None
        self.button_caption = None  # button caption
        self.is_signed = None  # True / False if signature
        self.text_color = (0, 0, 0)
        self.text_font = "Helv"
        self.text_fontsize = 0
        self.text_maxlen = 0  # text fields only
        self.text_format = 0  # text fields only
        self._text_da = ""  # /DA = default appearance

        self.script = None  # JavaScript (/A)
        self.script_stroke = None  # JavaScript (/AA/K)
        self.script_format = None  # JavaScript (/AA/F)
        self.script_change = None  # JavaScript (/AA/V)
        self.script_calc = None  # JavaScript (/AA/C)
        self.script_blur = None  # JavaScript (/AA/Bl)
        self.script_focus = None  # JavaScript (/AA/Fo) codespell:ignore

        self.rect = None  # annot value
        self.xref = 0  # annot value

    def __repr__(self):
        #return "'%s' widget on %s" % (self.field_type_string, str(self.parent))
        # No self.parent.
        return f'Widget:(field_type={self.field_type_string} script={self.script})'
        return "'%s' widget" % (self.field_type_string)

    def _adjust_font(self):
        """Ensure text_font is from our list and correctly spelled.
        """
        if not self.text_font:
            self.text_font = "Helv"
            return
        valid_fonts = ("Cour", "TiRo", "Helv", "ZaDb")
        for f in valid_fonts:
            if self.text_font.lower() == f.lower():
                self.text_font = f
                return
        self.text_font = "Helv"
        return

    def _checker(self):
        """Any widget type checks.
        """
        if self.field_type not in range(1, 8):
            raise ValueError("bad field type")

        # if setting a radio button to ON, first set Off all buttons
        # in the group - this is not done by MuPDF:
        if self.field_type == mupdf.PDF_WIDGET_TYPE_RADIOBUTTON and self.field_value not in (False, "Off") and hasattr(self, "parent"):
            # so we are about setting this button to ON/True
            # check other buttons in same group and set them to 'Off'
            doc = self.parent.parent
            kids_type, kids_value = doc.xref_get_key(self.xref, "Parent/Kids")
            if kids_type == "array":
                xrefs = tuple(map(int, kids_value[1:-1].replace("0 R","").split()))
                for xref in xrefs:
                    if xref != self.xref:
                        doc.xref_set_key(xref, "AS", "/Off")
        # the calling method will now set the intended button to on and
        # will find everything prepared for correct functioning.

    def _parse_da(self):
        """Extract font name, size and color from default appearance string (/DA object).

        Equivalent to 'pdf_parse_default_appearance' function in MuPDF's 'pdf-annot.c'.
        """
        if not self._text_da:
            return
        font = "Helv"
        fsize = 0
        col = (0, 0, 0)
        dat = self._text_da.split()  # split on any whitespace
        for i, item in enumerate(dat):
            if item == "Tf":
                font = dat[i - 2][1:]
                fsize = float(dat[i - 1])
                dat[i] = dat[i-1] = dat[i-2] = ""
                continue
            if item == "g":  # unicolor text
                col = [(float(dat[i - 1]))]
                dat[i] = dat[i-1] = ""
                continue
            if item == "rg":  # RGB colored text
                col = [float(f) for f in dat[i - 3:i]]
                dat[i] = dat[i-1] = dat[i-2] = dat[i-3] = ""
                continue
        self.text_font = font
        self.text_fontsize = fsize
        self.text_color = col
        self._text_da = ""
        return

    def _validate(self):
        """Validate the class entries.
        """
        if (self.rect.is_infinite
            or self.rect.is_empty
           ):
            raise ValueError("bad rect")

        if not self.field_name:
            raise ValueError("field name missing")

        if self.field_label == "Unnamed":
            self.field_label = None
        CheckColor(self.border_color)
        CheckColor(self.fill_color)
        if not self.text_color:
            self.text_color = (0, 0, 0)
        CheckColor(self.text_color)

        if not self.border_width:
            self.border_width = 0

        if not self.text_fontsize:
            self.text_fontsize = 0

        self.border_style = self.border_style.upper()[0:1]

        # standardize content of JavaScript entries
        btn_type = self.field_type in (
                mupdf.PDF_WIDGET_TYPE_BUTTON,
                mupdf.PDF_WIDGET_TYPE_CHECKBOX,
                mupdf.PDF_WIDGET_TYPE_RADIOBUTTON,
                )
        if not self.script:
            self.script = None
        elif type(self.script) is not str:
            raise ValueError("script content must be a string")

        # buttons cannot have the following script actions
        if btn_type or not self.script_calc:
            self.script_calc = None
        elif type(self.script_calc) is not str:
            raise ValueError("script_calc content must be a string")

        if btn_type or not self.script_change:
            self.script_change = None
        elif type(self.script_change) is not str:
            raise ValueError("script_change content must be a string")

        if btn_type or not self.script_format:
            self.script_format = None
        elif type(self.script_format) is not str:
            raise ValueError("script_format content must be a string")

        if btn_type or not self.script_stroke:
            self.script_stroke = None
        elif type(self.script_stroke) is not str:
            raise ValueError("script_stroke content must be a string")

        if btn_type or not self.script_blur:
            self.script_blur = None
        elif type(self.script_blur) is not str:
            raise ValueError("script_blur content must be a string")

        if btn_type or not self.script_focus:
            self.script_focus = None
        elif type(self.script_focus) is not str:
            raise ValueError("script_focus content must be a string")

        self._checker()  # any field_type specific checks

    def _sync_flags(self):
        """Propagate the field flags.

        If this widget has a "/Parent", set its field flags and that of all
        its /Kids widgets to the value of the current widget.
        Only possible for widgets existing in the PDF.

        Returns True or False.
        """
        if not self.xref:
            return False  # no xref: widget not in the PDF
        doc = self.parent.parent  # the owning document
        assert doc
        pdf = _as_pdf_document(doc)
        # load underlying PDF object
        pdf_widget = mupdf.pdf_load_object(pdf, self.xref)
        Parent = mupdf.pdf_dict_get(pdf_widget, PDF_NAME("Parent"))
        if not Parent.pdf_is_dict():
            return False  # no /Parent: nothing to do

        # put the field flags value into the parent field flags:
        Parent.pdf_dict_put_int(PDF_NAME("Ff"), self.field_flags)

        # also put that value into all kids of the Parent
        kids = Parent.pdf_dict_get(PDF_NAME("Kids"))
        if not kids.pdf_is_array():
            message("warning: malformed PDF, Parent has no Kids array")
            return False  # no /Kids: should never happen!

        for i in range(kids.pdf_array_len()):  # walk through all kids
            # access kid widget, and do some precautionary checks
            kid = kids.pdf_array_get(i)
            if not kid.pdf_is_dict():
                continue
            xref = kid.pdf_to_num()  # get xref of the kid
            if xref == self.xref:  # skip self widget
                continue
            subtype = kid.pdf_dict_get(PDF_NAME("Subtype"))
            if not subtype.pdf_to_name() == "Widget":
                continue
            # put the field flags value into the kid field flags:
            kid.pdf_dict_put_int(PDF_NAME("Ff"), self.field_flags)

        return True  # all done

    def button_states(self):
        """Return the on/off state names for button widgets.

        A button may have 'normal' or 'pressed down' appearances. While the 'Off'
        state is usually called like this, the 'On' state is often given a name
        relating to the functional context.
        """
        if self.field_type not in (2, 5):
            return None  # no button type
        if hasattr(self, "parent"):  # field already exists on page
            doc = self.parent.parent
        else:
            return
        xref = self.xref
        states = {"normal": None, "down": None}
        APN = doc.xref_get_key(xref, "AP/N")
        if APN[0] == "dict":
            nstates = []
            APN = APN[1][2:-2]
            apnt = APN.split("/")[1:]
            for x in apnt:
                nstates.append(x.split()[0])
            states["normal"] = nstates
        if APN[0] == "xref":
            nstates = []
            nxref = int(APN[1].split(" ")[0])
            APN = doc.xref_object(nxref)
            apnt = APN.split("/")[1:]
            for x in apnt:
                nstates.append(x.split()[0])
            states["normal"] = nstates
        APD = doc.xref_get_key(xref, "AP/D")
        if APD[0] == "dict":
            dstates = []
            APD = APD[1][2:-2]
            apdt = APD.split("/")[1:]
            for x in apdt:
                dstates.append(x.split()[0])
            states["down"] = dstates
        if APD[0] == "xref":
            dstates = []
            dxref = int(APD[1].split(" ")[0])
            APD = doc.xref_object(dxref)
            apdt = APD.split("/")[1:]
            for x in apdt:
                dstates.append(x.split()[0])
            states["down"] = dstates
        return states

    @property
    def next(self):
        return self._annot.next

    def on_state(self):
        """Return the "On" value for button widgets.
        
        This is useful for radio buttons mainly. Checkboxes will always return
        "Yes". Radio buttons will return the string that is unequal to "Off"
        as returned by method button_states().
        If the radio button is new / being created, it does not yet have an
        "On" value. In this case, a warning is shown and True is returned.
        """
        if self.field_type not in (2, 5):
            return None  # no checkbox or radio button
        bstate = self.button_states()
        if bstate is None:
            bstate = dict()
        for k in bstate.keys():
            for v in bstate[k]:
                if v != "Off":
                    return v
        message("warning: radio button has no 'On' value.")
        return True

    def reset(self):
        """Reset the field value to its default.
        """
        TOOLS._reset_widget(self._annot)

    def update(self, sync_flags=False):
        """Reflect Python object in the PDF."""
        self._validate()

        self._adjust_font()  # ensure valid text_font name

        # now create the /DA string
        self._text_da = ""
        if   len(self.text_color) == 3:
            fmt = "{:g} {:g} {:g} rg /{f:s} {s:g} Tf" + self._text_da
        elif len(self.text_color) == 1:
            fmt = "{:g} g /{f:s} {s:g} Tf" + self._text_da
        elif len(self.text_color) == 4:
            fmt = "{:g} {:g} {:g} {:g} k /{f:s} {s:g} Tf" + self._text_da
        self._text_da = fmt.format(*self.text_color, f=self.text_font,
                                    s=self.text_fontsize)
        # finally update the widget

        # if widget has a '/AA/C' script, make sure it is in the '/CO'
        # array of the '/AcroForm' dictionary.
        if self.script_calc:  # there is a "calculation" script:
            # make sure we are in the /CO array
            util_ensure_widget_calc(self._annot)

        # finally update the widget
        TOOLS._save_widget(self._annot, self)
        self._text_da = ""
        if sync_flags:
            self._sync_flags()  # propagate field flags to parent and kids
