import pytest
from py_algorithms.array import new_circular_array

@pytest.fixture
def arr():
    """Fixture to create a CircularArray instance with size 5."""
    return new_circular_array(5)

def test_enqueue_and_size(arr):
    """Test that enqueueing elements updates teh size correctly."""
    for i in range(5):
        arr.enqueue(i)
    assert arr.size() == 5

def test_dequeue_and_size(arr):
    """Test that dequeueing elements decreases the size correctly."""
    for i in range(5):
        arr.enqueue(i)
    for _ in range(3):    
        arr.dequeue()
    assert arr.size() == 2

def test_resizing():
    """Test automatic resizing when the array is full."""
    arr = new_circular_array(5)
    
    for i in range(10):
        arr.enqueue(i)
    assert arr.size() == 10
    assert len(arr._list) == 20
    # data=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, None, None, None, None, None, None, None, None, None, None]

def test_dequeue_empty():
    """Test dequeueing from an empty array raises an error."""
    arr = new_circular_array(5)

    # Calling arr.dequeue() raises a RuntimeError with the message "Empty" when the circular array is empty.
    with pytest.raises(RuntimeError, match="Empty"):
        arr.dequeue()

def test_circular_behavior():
    """Test that elements wrap around correctly."""
    arr = new_circular_array(5)

    for i in range(4):
        arr.enqueue(i)
    arr.dequeue()
    arr.enqueue(99)
    assert arr._list[arr._rear - 1] == 99 # The last inserted should be 99

def test_str_representation():
    """Test the __str__ method for human-readable output."""
    arr = new_circular_array(5)
    arr.enqueue(1)
    arr.enqueue(2)
    arr.enqueue(3)
    assert str(arr) == "1 -> 2 -> 3"

def test_repr_representation():
    """Test the __repr__ method for debugging."""
    arr = new_circular_array(3)
    arr.enqueue(1)
    arr.enqueue(2)
    expected_repr = "CircularArray(front=0, rear=2, size=2, data=[1, 2, None])"
    assert repr(arr) == expected_repr

def f():
    raise SystemExit(1)
    #raise 1 => FAILED

def test_f_raises_system_exit_exception():
    with pytest.raises(SystemExit):
        f()



