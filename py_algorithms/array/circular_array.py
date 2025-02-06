class CircularArray:
    __slots__ = '_list', '_front', '_rear', '_n' # it is intended to be private
    # Attributes:
    # _list → The array storing elements
    # _front → The index of the front (oldest) element
    # _rear → The index of the next empty slot
    # _n → The total capacity of the array

    def __init__(self,n):
        self._list = [None for _ in range(n)] # is an array of None values
        self._n = n 
        self._front = 0 # the queue starts empty
        self._rear = 0 # the queue starts empty

    def size(self): # Computes the current number of elements in the queue
        if self._rear >= self._front:
            return self._rear - self._front
        return self._n - (self._front - self._rear) # remaining part of the list from _front to end plus the part from the beginning to _rear

    def enqueue(self, item):
        size = self.size()
        if size == self._n - 1: # Checks if the queue is full 
            self._resize(lambda x: x * 2) ## doubling the capacity
        self._list[self._rear] = item
        self._rear = (self._rear + 1) % self._n # updates _rear => ensures circular behavior when inserting an element.

    def dequeue(self):
        size = self.size()
        if size == 0:
            raise RuntimeError("Empty")
        data = self._list[self._front]
        self._list[self._front] = float("inf") # Sets the dequeued position to float("inf") (for debugging)
        self._front = (self._front + 1) % self._n # Moves _front to the next position
        return data

    def _resize(self, strategy_f):
        new_size = strategy_f(self._n) ## which calls lambda x: x * 2.
        xs = [None for _ in range(new_size)]
        i = self._front
        j = 0
        while i != self._rear:
            xs[j] = self._list[i] # Copies elements into a new list while maintaining order.
            i = (i+1) % self._n
            j += 1

        self._front = 0
        self._rear = j
        self._n = new_size
        self._list = xs

    # Add __str__ method for readable output
    def __str__(self):
        if self.size()==0:
            return "CircularArray is empty"
        elements = []
        i = self._front
        while i != self._rear:
            elements.append(str(self._list[i]))
            i = (i + 1) % self._n
        return " -> ".join(elements)
    
    # Add __repr__ method for debugging
    def __repr__(self):
        return f"CircularArray(front={self._front}, rear={self._rear}, size={self.size()}, data={self._list})"


if __name__ == '__main__':
    arr = CircularArray(5)
    arr.enqueue(1)
    arr.enqueue(2)
    arr.enqueue(3)
    print(arr.dequeue())
    print(arr.dequeue())
    arr.enqueue(9)
    arr.enqueue(4)
    arr.enqueue(5)
    arr.enqueue(6)
    arr.enqueue(7) # forces a resize 
    arr.enqueue(8)
    # print(arr._list) # Not good => Direct access to a private attribute
    print(arr) # Uses __str__
    print(repr(arr)) # Uses __repr__ 


