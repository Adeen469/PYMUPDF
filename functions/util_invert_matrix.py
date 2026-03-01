"""
Function: fitz.util_invert_matrix
Signature: util_invert_matrix(matrix)
Description: No docstring available.
"""

import fitz

# Source code of fitz.util_invert_matrix:
def util_invert_matrix(matrix):
    if 0:
        # Use MuPDF's fz_invert_matrix().
        if isinstance( matrix, (tuple, list)):
            matrix = mupdf.FzMatrix( *matrix)
        elif isinstance( matrix, mupdf.fz_matrix):
            matrix = mupdf.FzMatrix( matrix)
        elif isinstance( matrix, Matrix):
            matrix = mupdf.FzMatrix( matrix.a, matrix.b, matrix.c, matrix.d, matrix.e, matrix.f)
        assert isinstance( matrix, mupdf.FzMatrix), f'{type(matrix)=}: {matrix}'
        ret = mupdf.fz_invert_matrix( matrix)
        if ret == matrix and (0
                or abs( matrix.a - 1) >= sys.float_info.epsilon
                or abs( matrix.b - 0) >= sys.float_info.epsilon
                or abs( matrix.c - 0) >= sys.float_info.epsilon
                or abs( matrix.d - 1) >= sys.float_info.epsilon
                ):
            # Inversion not possible.
            return 1, ()
        return 0, (ret.a, ret.b, ret.c, ret.d, ret.e, ret.f)
    # Do inversion in python.
    src = JM_matrix_from_py(matrix)
    a = src.a
    det = a * src.d - src.b * src.c
    if det < -sys.float_info.epsilon or det > sys.float_info.epsilon:
        dst = mupdf.FzMatrix()
        rdet = 1 / det
        dst.a = src.d * rdet
        dst.b = -src.b * rdet
        dst.c = -src.c * rdet
        dst.d = a * rdet
        a = -src.e * dst.a - src.f * dst.c
        dst.f = -src.e * dst.b - src.f * dst.d
        dst.e = a
        return 0, (dst.a, dst.b, dst.c, dst.d, dst.e, dst.f)

    return 1, ()
