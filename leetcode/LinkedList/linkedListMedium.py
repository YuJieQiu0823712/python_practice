from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # For testing equality of linked lists
    def __eq__(self, other):
        if not isinstance(other,ListNode):
            return False
        return self.val == other.val and self.next == other.next

    def __repr__(self):
        return f"{self.val} -> {self.next}"

class Node:
    def __init__(self, val, left=None, right =None):
        self.val = val
        self.left = left
        self.right = right

class MediumSolution:
    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Add two numbers represented by two singly-linked lists.

        Each linked list represents a non-negative integer in reverse order, where each node contains a single digit.
        The task is to compute their sum and return it as a linked list in the same reverse order format.

        args:
            l1 (Optional[ListNode]): The head of the first linked list
            l2 (Optional[ListNode]): The head of the second linked list

        Returns:
            Optional[ListNode]: The head of the linked list representing the sum

        TC: O(n)
        SC: O(1)    
        """
        if not l1:
            return l2
        if not l2:
            return l1
        dummy = ListNode(-1)
        head = dummy
        carry = 0

        while l1 and l2:
            head.next = ListNode((l1.val + l2.val + carry) % 10)
            carry = (l1.val + l2.val + carry) // 10
            l1 = l1.next
            l2 = l2.next
            head = head.next

        while l1:
            head.next = ListNode((l1.val + carry) % 10)
            carry = (l1.val + carry) // 10
            l1 = l1.next
            head = head.next
        
        while l2:
            head.next = ListNode((l2.val + carry) % 10)
            carry = (l2.val + carry) // 10
            l2 = l2.next
            head = head.next

        if carry == 1:
            head.next = ListNode(1)
        
        return dummy.next

    def convertBinarySearchTreeToSortedDoublyLinkedList426(self, root: 'Node') -> 'Node':
        """
        Converts a Binary Search Tree (BST) to a circular, sorted, doubly linked list in-place.

        Each node's left and right pointers are used as the previous and next pointers in the resulting doubly linked list.
        The in-order traversal of the BST is used to maintain the ascending order in the list.

        If the BST is empty (i.e., root is None), the function returns None.

        Args:
            root (Node): The root of the binary search tree.

        Returns:
            Node: The head of the circular, sorted, doubly linked list.
            
        TC: O(n)
        SC: O(n)  
        """
        # 1 recursive
        # edge case
        if not root:
            return

        self.prev = None
        self.head = None

        def in_order(curr):
            # base case
            if not curr:
                return

            in_order(curr.left)
            if not self.prev:
                self.head = curr
            else:
                self.prev.right = curr
                curr.left = self.prev
            self.prev = curr
            in_order(curr.right)

        in_order(root)
        self.prev.right = self.head
        self.head.left = self.prev
        return self.head

        # 2 iterative (if tree is really big use this strategy, otherwise it may has stack overflow)
        # if not root:
        #     return
        
        # prev = None
        # head = None

        # stack = [] 
        # # LIFO => Python has a default recursion limit of around 1000 
        # # (often 996–998 or 987, depending on your system and version).
        
        # curr = root

        # while stack or cuur:
        #     while curr:
        #         stack.append(curr)
        #         curr = curr.left
        #     curr = stack.pop()
        #     if not prev:
        #         head = curr
        #     else:
        #         prev.right = curr
        #         curr.left = prev
        #     prev = curr
        #     curr = curr.right
        # head.left = prev
        # prev.right = head
        # return head





class DesignLinkedList707:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = ListNode(-1)
        self.length = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, retrun -1.
        TC: O(n)
        SC: O(1)
        """
        if index < 0 or index >= self.length:
            return -1
        dummy_head = self.head

        for _ in range(index + 1):
            dummy_head = dummy_head.next

        return dummy_head.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. 
        After the insertion, the new node will be the head of the linked list.
        TC: O(1)
        SC: O(1) 
        """
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        TC: O(n)
        SC: O(1) 
        """
        dummy_head = self.head
        new_node = ListNode(val)

        for _ in range(self.length):
            dummy_head = dummy_head.next

        dummy_head.next = new_node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. 
        If index equals to the length of linked list will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        TC: O(n)
        SC: O(1) 
        """
        dummy_head = self.head
        new_node = ListNode(val)

        for _ in range(index):
            dummy_head = dummy_head.next

        new_node.next = dummy_head.next
        dummy_head.next = new_node
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        TC: O(n)
        SC: O(1) 
        """
        if index < 0 or index >= self.length:
            return

        dummy_head = self.head
        for _ in range(index):
            dummy_head = dummy_head.next
        dummy_head.next = dummy_head.next.next
        self.length -= 1