__all__ = [
    'new_boyer_moore_find'
]

from typing import Callable
from .boyer_moore_find import BoyerMooreFind

def new_boyer_moore_find() -> Callable[[str,str],int]:
    # Takes two str arguments (the main string and the substring).
    # Returns an int (the starting index of the match, or -1 if not found).
    return BoyerMooreFind()
