class CircularArray:
    __slots__ = '_list', '_front', '_rear', '_n'

    def __init__(self,n):
        self.list = [None for _ in range(n)]
        
