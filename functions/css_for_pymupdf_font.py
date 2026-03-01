"""
Function: fitz.css_for_pymupdf_font
Signature: css_for_pymupdf_font(fontcode: str, *, CSS: Optional[str] = None, archive: Any = None, name: Optional[str] = None) -> str
Description:
Create @font-face items for the given fontcode of pymupdf-fonts.

Adds @font-face support for fonts contained in package pymupdf-fonts.

Creates a CSS font-family for all fonts starting with string 'fontcode'.

Note:
    The font naming convention in package pymupdf-fonts is "fontcode<sf>",
    where the suffix "sf" is either empty or one of "it", "bo" or "bi".
    These suffixes thus represent the regular, italic, bold or bold-italic
    variants of a font. For example, font code "notos" refers to fonts
    "notos" - "Noto Sans Regular"
    "notosit" - "Noto Sans Italic"
    "notosbo" - "Noto Sans Bold"
    "notosbi" - "Noto Sans Bold Italic"

    This function creates four CSS @font-face definitions and collectively
    assigns the font-family name "notos" to them (or the "name" value).

All fitting font buffers of the pymupdf-fonts package are placed / added
to the archive provided as parameter.
To use the font in pymupdf.Story, execute 'set_font(fontcode)'. The correct
font weight (bold) or style (italic) will automatically be selected.
Expects and returns the CSS source, with the new CSS definitions appended.

Args:
    fontcode: (str) font code for naming the font variants to include.
              E.g. "fig" adds notos, notosi, notosb, notosbi fonts.
              A maximum of 4 font variants is accepted.
    CSS: (str) CSS string to add @font-face definitions to.
    archive: (Archive, mandatory) where to place the font buffers.
    name: (str) use this as family-name instead of 'fontcode'.
Returns:
    Modified CSS, with appended @font-face statements for each font variant
    of fontcode.
    Fontbuffers associated with "fontcode" will be added to 'archive'.
"""

import fitz

# Source code of fitz.css_for_pymupdf_font:
def css_for_pymupdf_font(
    fontcode: str, *, CSS: OptStr = None, archive: AnyType = None, name: OptStr = None
) -> str:
    """Create @font-face items for the given fontcode of pymupdf-fonts.

    Adds @font-face support for fonts contained in package pymupdf-fonts.

    Creates a CSS font-family for all fonts starting with string 'fontcode'.

    Note:
        The font naming convention in package pymupdf-fonts is "fontcode<sf>",
        where the suffix "sf" is either empty or one of "it", "bo" or "bi".
        These suffixes thus represent the regular, italic, bold or bold-italic
        variants of a font. For example, font code "notos" refers to fonts
        "notos" - "Noto Sans Regular"
        "notosit" - "Noto Sans Italic"
        "notosbo" - "Noto Sans Bold"
        "notosbi" - "Noto Sans Bold Italic"

        This function creates four CSS @font-face definitions and collectively
        assigns the font-family name "notos" to them (or the "name" value).

    All fitting font buffers of the pymupdf-fonts package are placed / added
    to the archive provided as parameter.
    To use the font in pymupdf.Story, execute 'set_font(fontcode)'. The correct
    font weight (bold) or style (italic) will automatically be selected.
    Expects and returns the CSS source, with the new CSS definitions appended.

    Args:
        fontcode: (str) font code for naming the font variants to include.
                  E.g. "fig" adds notos, notosi, notosb, notosbi fonts.
                  A maximum of 4 font variants is accepted.
        CSS: (str) CSS string to add @font-face definitions to.
        archive: (Archive, mandatory) where to place the font buffers.
        name: (str) use this as family-name instead of 'fontcode'.
    Returns:
        Modified CSS, with appended @font-face statements for each font variant
        of fontcode.
        Fontbuffers associated with "fontcode" will be added to 'archive'.
    """
    # @font-face template string
    CSSFONT = "\n@font-face {font-family: %s; src: url(%s);%s%s}\n"

    if not type(archive) is Archive:
        raise ValueError("'archive' must be an Archive")
    if CSS is None:
        CSS = ""

    # select font codes starting with the pass-in string
    font_keys = [k for k in fitz_fontdescriptors.keys() if k.startswith(fontcode)]
    if font_keys == []:
        raise ValueError(f"No font code '{fontcode}' found in pymupdf-fonts.")
    if len(font_keys) > 4:
        raise ValueError("fontcode too short")
    if name is None:  # use this name for font-family
        name = fontcode

    for fkey in font_keys:
        font = fitz_fontdescriptors[fkey]
        bold = font["bold"]  # determine font property
        italic = font["italic"]  # determine font property
        fbuff = font["loader"]()  # load the fontbuffer
        archive.add(fbuff, fkey)  # update the archive
        bold_text = "font-weight: bold;" if bold else ""
        italic_text = "font-style: italic;" if italic else ""
        CSS += CSSFONT % (name, fkey, bold_text, italic_text)
    return CSS
