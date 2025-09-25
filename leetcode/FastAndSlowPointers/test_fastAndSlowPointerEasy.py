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

def build_linked_list(values):
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def linked_list_to_list(node: ListNode):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

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


@pytest.mark.parametrize("head_list, expected", [
        ([1, 2, 3, 4, 5], [3, 4, 5]),
        ([1, 2, 3, 4, 5, 6], [4, 5, 6]),
        ([1], [1]),
        ([1, 2], [2]),
])
def test_middleOfTheLinkedList876(head_list, expected):
    head = build_linked_list(head_list)
    e = EasySolution()
    result = e.middleOfTheLinkedList876(head)
    assert linked_list_to_list(result) == expected