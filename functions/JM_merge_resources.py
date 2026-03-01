"""
Function: fitz.JM_merge_resources
Signature: JM_merge_resources(page, temp_res)
Description:
Merge the /Resources object created by a text pdf device into the page.
The device may have created multiple /ExtGState/Alp? and /Font/F? objects.
These need to be renamed (renumbered) to not overwrite existing page
objects from previous executions.
Returns the next available numbers n, m for objects /Alp<n>, /F<m>.
"""

import fitz

# Source code of fitz.JM_merge_resources:
def JM_merge_resources( page, temp_res):
    '''
    Merge the /Resources object created by a text pdf device into the page.
    The device may have created multiple /ExtGState/Alp? and /Font/F? objects.
    These need to be renamed (renumbered) to not overwrite existing page
    objects from previous executions.
    Returns the next available numbers n, m for objects /Alp<n>, /F<m>.
    '''
    # page objects /Resources, /Resources/ExtGState, /Resources/Font
    resources = mupdf.pdf_dict_get(page.obj(), PDF_NAME('Resources'))
    if not resources.m_internal:
        resources = mupdf.pdf_dict_put_dict(page.obj(), PDF_NAME('Resources'), 5)
    main_extg = mupdf.pdf_dict_get(resources, PDF_NAME('ExtGState'))
    main_fonts = mupdf.pdf_dict_get(resources, PDF_NAME('Font'))

    # text pdf device objects /ExtGState, /Font
    temp_extg = mupdf.pdf_dict_get(temp_res, PDF_NAME('ExtGState'))
    temp_fonts = mupdf.pdf_dict_get(temp_res, PDF_NAME('Font'))

    max_alp = -1
    max_fonts = -1

    # Handle /Alp objects
    if mupdf.pdf_is_dict(temp_extg):   # any created at all?
        n = mupdf.pdf_dict_len(temp_extg)
        if mupdf.pdf_is_dict(main_extg):   # does page have /ExtGState yet?
            for i in range(mupdf.pdf_dict_len(main_extg)):
                # get highest number of objects named /Alpxxx
                alp = mupdf.pdf_to_name( mupdf.pdf_dict_get_key(main_extg, i))
                if not alp.startswith('Alp'):
                    continue
                j = mupdf.fz_atoi(alp[3:])
                if j > max_alp:
                    max_alp = j
        else:   # create a /ExtGState for the page
            main_extg = mupdf.pdf_dict_put_dict(resources, PDF_NAME('ExtGState'), n)

        max_alp += 1
        for i in range(n):  # copy over renumbered /Alp objects
            alp = mupdf.pdf_to_name( mupdf.pdf_dict_get_key( temp_extg, i))
            j = mupdf.fz_atoi(alp[3:]) + max_alp
            text = f'Alp{j}'
            val = mupdf.pdf_dict_get_val( temp_extg, i)
            mupdf.pdf_dict_puts(main_extg, text, val)

    if mupdf.pdf_is_dict(main_fonts):  # has page any fonts yet?
        for i in range(mupdf.pdf_dict_len(main_fonts)):    # get max font number
            font = mupdf.pdf_to_name( mupdf.pdf_dict_get_key( main_fonts, i))
            if not font.startswith("F"):
                continue
            j = mupdf.fz_atoi(font[1:])
            if j > max_fonts:
                max_fonts = j
    else:   # create a Resources/Font for the page
        main_fonts = mupdf.pdf_dict_put_dict(resources, PDF_NAME('Font'), 2)

    max_fonts += 1
    for i in range(mupdf.pdf_dict_len(temp_fonts)):    # copy renumbered fonts
        font = mupdf.pdf_to_name( mupdf.pdf_dict_get_key( temp_fonts, i))
        j = mupdf.fz_atoi(font[1:]) + max_fonts
        text = f'F{j}'
        val = mupdf.pdf_dict_get_val(temp_fonts, i)
        mupdf.pdf_dict_puts(main_fonts, text, val)
    return (max_alp, max_fonts) # next available numbers
