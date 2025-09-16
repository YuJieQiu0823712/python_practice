class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class EasySolution:
    def linkedListCycle141(head):
        slow = fast = head
        # slow = head
        # fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                return True
        return False