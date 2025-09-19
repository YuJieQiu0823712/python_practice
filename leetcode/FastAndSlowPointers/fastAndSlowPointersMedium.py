class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None

class MediumSolution:
    def linkedListCycleII142(self, head: ListNode) -> ListNode:
        """
        Return the node where the cycle begins.

        TC: O(n)
        SC: O(1)
        """
        if not head:
            return None
        
        def find_meet(head: ListNode) -> ListNode:
            slow = fast = head

            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next

                if slow == fast:
                    return slow
            return None # no cycle
        
        meet_point = find_meet(head)
        new_point = head

        if meet_point == None:
            return None

        while meet_point != new_point:
            meet_point = meet_point.next
            new_point = new_point.next

        return meet_point
        



