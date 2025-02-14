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

        
