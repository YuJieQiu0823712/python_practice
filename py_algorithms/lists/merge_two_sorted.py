class Node:
    __slots__ = '_data', '_next'

    def __init__(self, data, successor):
        self._data = data
        self._next = successor
    
    @property
    def data(self):
        return self._data
    
    @property
    def next(self):
        return self._next
    
    @next.setter
    def next(self, other: 'Node'): # 'Node' is used as a forward reference to avoid issues with the class not being fully defined yet.
        if other is None:
            self._next = None
            return
        
        if not isinstance(other, self.__class__):
            raise ValueError("Type invariant violation.")
        
        self._next = other
    
    def __repr__(self):
        return '#<{} data={} next={}>' \
        .format(self.__class__.__name__, self.data, self.next)

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


