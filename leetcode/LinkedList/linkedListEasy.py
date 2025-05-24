from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class EasySolution:
    def linkedListCycle141(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                return True
        
        return False

    def mergeTwoSortedLists21(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge two sorted singly linked lists into one sorted linked list.

        args:
            list1 (Optional[ListNode]): The head of the first sorted linked list.
            list2 (Optional[ListNode]): The head of the second sorted linked list.

        Returns:
            Optional[ListNode]: The head of the merged sorted linked list.

        TC: O(n)
        SC: O(1)
        """
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # One of the lists may still have nodes left
        tail.next = list1 if list1 else list2
        return dummy.next


        # i = 0
        # j = 0
        # while i < len(list1) and j < len(list2):
        #     if list2[j] >= list1[i]:
        #         result.append(list1[i])
        #         i += 1
        #     else:
        #         result.append(list2[j])
        #         j += 1
        # result.extend(list1[i:])
        # result.extend(list2[j:])
        # return result

        # TC: O(n)
        # SC: O(n)


    