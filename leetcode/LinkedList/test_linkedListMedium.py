import pytest
from linkedListMedium import MediumSolution, ListNode, Node, DesignLinkedList707, LRUCache146


# Helper to convert list to linked list
def list_to_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Helper to convert linked list to list
def linked_list_to_list(ListNode):
    result = []
    while ListNode:
        result.append(ListNode.val)
        ListNode = ListNode.next
    return result

# Helper to convert doubly linked list to list
def doubly_linked_list_to_list(head: Node, count=100):
    if not head:
        return []
    result = []
    curr = head
    for _ in range(count):
        result.append(curr.val)
        curr = curr.right
        if curr == head:
            break
    return result


@pytest.mark.parametrize("l1_vals, l2_vals, expected", [
    ([2,4,3],[5,6,4],[7,0,8]),
    ([9,9,9],[1],[0,0,0,1]),
    ([1,8],[0],[1,8])
])

def test_addTwoNumbers2(l1_vals, l2_vals, expected):
    m = MediumSolution()
    l1 = list_to_linked_list(l1_vals)
    l2 = list_to_linked_list(l2_vals)
    result = linked_list_to_list(m.addTwoNumbers2(l1,l2))
    assert result == expected


@pytest.mark.parametrize("tree_nodes, expected",[
    (Node(4, Node(2, Node(1), Node(3)), Node(5)),  [1, 2, 3, 4, 5]),
    (Node(10, None, Node(20, None, Node(30))), [10, 20, 30])
])

def test_convertBinarySearchTreeToSortedDoublyLinkedList426(tree_nodes, expected):
    m = MediumSolution()
    head = m.convertBinarySearchTreeToSortedDoublyLinkedList426(tree_nodes)
    result = doubly_linked_list_to_list(head)
    assert result == expected


def test_DesignLinkedList707():
    myLinkedList = DesignLinkedList707()
    assert myLinkedList.addAtHead(1) is None
    assert myLinkedList.addAtTail(3) is None
    assert myLinkedList.addAtIndex(1, 2) is None  # List: 1->2->3
    assert myLinkedList.get(1) == 2
    assert myLinkedList.deleteAtIndex(1) is None  # List becomes: 1->3
    assert myLinkedList.get(1) == 3


def test_LRUCache146():
    lru = LRUCache146(2)
    lru.put(1, 1)                     # cache: {1=1}
    lru.put(2, 2)                     # cache: {1=1, 2=2}
    assert lru.get(1) == 1           # cache: {2=2, 1=1}
    lru.put(3, 3)                     # evicts key 2, cache: {1=1, 3=3}
    assert lru.get(2) == -1
    lru.put(4, 4)                     # evicts key 1, cache: {3=3, 4=4}
    assert lru.get(1) == -1
    assert lru.get(3) == 3
    assert lru.get(4) == 4