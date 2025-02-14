from .node import Node

class MergeTwoSorted:
    @staticmethod
    def apply(a:Node, b:Node) -> Node:
        ptr = Node(-1,None) # dummy node
        head = ptr # pointer
        
        # Iterate Through Both Lists (a and b)
        while a is not None and b is not None:
            if a.data < b.data:
                head.next = a
                a = a.next # renew data of a to the next element
            else:
                head.next = b
                b = b.next

            head = head.next # head moves forward to keep track of the last node in the merged list.
        
        # Attach the Remaining Nodes
        if a:
            head.next = a
        if b:
            head.next = b
        return ptr.next # Return the head of the merged linked list, skipping the dummy node


        # a = [1,3,5]
        # b = [2,4,6]

        ## Step 1: Initialize ptr (Dummy Node)
        #
        # ptr (-1) → None
        # head (points to ptr)

        ## Step 2: Compare a.data and b.data
        ## 1 < 2 → Attach a
        #
        # ptr (-1) → 1 → None
        # head        ↑
        # a     (1) → 3 → 5
        # b     (2) → 4 → 6


