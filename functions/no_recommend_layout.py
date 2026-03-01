"""
Function: fitz.no_recommend_layout
Signature: no_recommend_layout()
Description:
For users who never want to see the layout recommendation.
"""

import fitz

# Source code of fitz.no_recommend_layout:
def no_recommend_layout():
    """For users who never want to see the layout recommendation."""
    global _recommend_layout
    _recommend_layout = False
