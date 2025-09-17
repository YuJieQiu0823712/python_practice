import pytest
from fastAndSlowPointersEasy import ListNode, EasySolution

def create_linked_list(values, pos):
    """Helper function to create a linked list with a cycle."""
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(values) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]



@pytest.mark.parametrize("values, pos, expected", [
    ([3,2,0,-4], 1,True),
    ([1,2], 0, True),
    ([1], -1, False)
])

def test_linkedListCycle141(values, pos, expected):
    head = create_linked_list(values,pos)
    e = EasySolution()
    result = e.linkedListCycle141(head)
    assert result == expected
