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


@pytest.mark.parametrize("l1_vals, l2_vals, expected", [
    ([1,2,5], [2,4,6], [1,2,2,4,5,6]),
    ([], [], []),
    ([], [0], [0])
])

def test_mergeTwoSortedLists21(l1_vals, l2_vals, expected):
    e = EasySolution()
    l1 = list_to_linked_list(l1_vals)
    l2 = list_to_linked_list(l2_vals)
    result = linked_list_to_list(e.mergeTwoSortedLists2(l1, l2))
    assert result == expected

