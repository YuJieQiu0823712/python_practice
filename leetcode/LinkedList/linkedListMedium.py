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

# class DesignLinkedList:
#     def __init__(self):

#     def get(self, index: int) -> int:
        

#     def addAtHead(self, val: int) -> None:
        

#     def addAtTail(self, val: int) -> None:
        

#     def addAtIndex(self, index: int, val: int) -> None:
        

#     def deleteAtIndex(self, index: int) -> None: