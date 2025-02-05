__all__ = [
    'new_circular_array'
]

from .circular_array import CircularArray

def new_circular_array(size: int = 5) -> CircularArray:
    """
    Factory method
    :param size: initial array size
    :return: CircularArray
    """
    # The factory method is useful when:
    # You want to abstract object creation.
    # The initialization logic is likely to change.
    # You may return different subclasses in the future.
    # You want to improve maintainability and readability.

    return CircularArray(size)


