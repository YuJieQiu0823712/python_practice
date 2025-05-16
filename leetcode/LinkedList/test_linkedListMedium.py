import pytest
from linkedListMedium import MediumSolution, ListNode

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
    ([2,4,3],[5,6,4],[7,0,8]),
    ([9,9,9],[1],[0,0,0,1])
    # ([1,8],[0],[1,8])
])

def test_addTwoNumbers2(l1_vals, l2_vals, expected):
    m = MediumSolution()
    l1 = list_to_linked_list(l1_vals)
    l2 = list_to_linked_list(l2_vals)
    result = linked_list_to_list(m.addTwoNumbers2(l1,l2))
    assert result == expected