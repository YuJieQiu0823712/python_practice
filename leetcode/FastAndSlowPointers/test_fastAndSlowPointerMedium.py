import pytest
from fastAndSlowPointersMedium import ListNode, MediumSolution

def create_linked_list(values, pos):
    """Helper function to create a linked list with a cycle."""
    if not values:
        return None, [] 
    nodes = [ListNode(v) for v in values]
    for i in range(len(values) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0], nodes  # return head and node list


@pytest.mark.parametrize("values, pos, expected_index", [
        ([3, 2, 0, -4], 1, 1),  # cycle starts at node index 1 (value=2)
        ([1, 2], 0, 0),         # cycle starts at head
        ([1], -1, None),        # no cycle
])
def test_linked_list_cycle(values, pos, expected_index):
    head, nodes = create_linked_list(values, pos)
    m = MediumSolution()
    result = m.linkedListCycleII142(head)
    if expected_index is None:
        assert result is None
    else:
        assert result == nodes[expected_index]