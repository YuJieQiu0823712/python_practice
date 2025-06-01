import pytest
from linkedListMedium import MediumSolution, ListNode, Node, RandomNode
from linkedListMedium import DesignLinkedList707, LRUCache146

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
        if curr is head:
            break
    return result

# Helper to build circular list
def build_circular_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        node = ListNode(val)
        curr.next = node
        curr = node
    curr.next = head # make it circular
    return head

# Helper to convert circular linked list to list
def to_list(head, limit=100):
    result = []
    curr = head
    for _ in range(limit):
        result.append(curr.val)
        curr = curr.next
        if curr is head: # not curr == head, this causes recursion
            break
    return result

# Helper to build random linked list
def build_random_list(node_data):

    if not node_data:
        return None

    nodes = [RandomNode(val) for val, _ in node_data]

    for i, (val, rand_idx) in enumerate(node_data):
        if i + 1 < len(nodes):
            nodes[i].next = nodes[i + 1]
        if rand_idx is not None:
            nodes[i].random = nodes[rand_idx]
    return nodes[0]

# Helper to convert to linked list with random pointer
def to_list_with_random(head):

    node_to_index = {}
    result = []
    curr = head
    index = 0

    # First pass: map nodes to indices
    while curr:
        node_to_index[curr] = index
        curr = curr.next
        index += 1

    # Second pass: build result list
    curr = head
    while curr:
        rand_idx = node_to_index[curr.random] if curr.random else None
        result.append([curr.val, rand_idx])
        curr = curr.next
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


@pytest.mark.parametrize("input_list, insert_val, expected_sorted", [
    ([5, 6, 2], 1, [1, 2, 5, 6]),
    ([5, 6, 2], 7, [2, 5, 6, 7])    
])

def test_insertIntoASortedCircularLinkedList708(input_list, insert_val, expected_sorted):
    m = MediumSolution()
    head = build_circular_list(input_list)
    new_head = m.insertIntoASortedCircularLinkedList708(head, insert_val)
    result = sorted(to_list(new_head))
    assert result == sorted(expected_sorted)


@pytest.mark.parametrize("input_list, expected_output", [
    (
        [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
        [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    ),
    (
        [[1, 1], [2, 1]],
        [[1, 1], [2, 1]]
    ),
])

def test_copyListWithRandomPointer138(input_list, expected_output):
    m = MediumSolution()
    head = build_random_list(input_list)
    copied_head = m.copyListWithRandomPointer138(head)
    result = to_list_with_random(copied_head)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"


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
    lru.put(1, 1)              # cache: {1=1}
    lru.put(2, 2)              # cache: {1=1, 2=2}
    assert lru.get(1) == 1     # cache: {2=2, 1=1}
    lru.put(3, 3)              # evicts key 2, cache: {1=1, 3=3}
    assert lru.get(2) == -1
    lru.put(4, 4)              # evicts key 1, cache: {3=3, 4=4}
    assert lru.get(1) == -1
    assert lru.get(3) == 3
    assert lru.get(4) == 4