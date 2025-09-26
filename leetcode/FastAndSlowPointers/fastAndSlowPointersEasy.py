class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class EasySolution:
    def linkedListCycle141(self, head):
        """
        TC: O(n)
        SC: O(1)
        """
        slow = fast = head
        # slow = head
        # fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                return True
        return False
    
    def middleOfTheLinkedList876(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def isHappy(self, n: int) -> bool:
        def find_square_sum(num: int) -> int:
            _curr_sum = 0

            while num > 0:
                digit = num % 10
                _curr_sum += digit ** 2
                num //= 10
            return _curr_sum
        
        slow = fast = n

        while True:
            slow = find_square_sum(slow)
            fast = find_square_sum(find_square_sum(fast))

            if slow == fast:
                break
        
        return slow == 1