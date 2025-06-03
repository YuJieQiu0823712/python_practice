import pytest
from linkedListEasy import EasySolution, ListNode

# Helper to convert list to linked list
def list_to_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Helper to convert linked list to list
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Helper function to create a linked list with a cycle
def create_cyclic_linked_list(values, pos):
    """
    Create a cyclic linked list from values.
    If pos >= 0, the last node will link to the node at index pos to form a cycle.
    """
    if not values:
        return None

    nodes = [ListNode(val) for val in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i+1]
    
    if pos != -1:
        nodes[-1].next = nodes[pos]
    
    return nodes[0]

@pytest.mark.parametrize("values, pos, expected", [
    ([3,2,0,4], 1, True), # cycle at node with value 2
    ([1,2,3], -1, False),  # no cycle
    ([1], -1, False) # single node, no cycle
])

def test_linkedListCycle141(values, pos, expected):
    e = EasySolution()
    head = create_cyclic_linked_list(values, pos)
    assert e.linkedListCycle141(head) == expected


@pytest.mark.parametrize("l1_vals, l2_vals, expected", [
    ([1,2,5], [2,4,6], [1,2,2,4,5,6]),
    ([], [], []),
    ([], [0], [0])
])

def test_mergeTwoSortedLists21(l1_vals, l2_vals, expected):
    e = EasySolution()
    l1 = list_to_linked_list(l1_vals)
    l2 = list_to_linked_list(l2_vals)
    result = linked_list_to_list(e.mergeTwoSortedLists21(l1, l2))
    assert result == expected


@pytest.mark.parametrize("input_list, val, expected_list", [
    ([1,2,6,3,4,5,6], 6, [1,2,3,4,5]),
    ([7,7,7,7], 7, []),
    ([], 1, [])
])

def test_removeLinkedListElements203(input_list, val, expected_list):
    e = EasySolution()
    head = list_to_linked_list(input_list)
    expected = list_to_linked_list(expected_list)
    result = e.removeLinkedListElements203(head, val)
    assert linked_list_to_list(result) == linked_list_to_list(expected)