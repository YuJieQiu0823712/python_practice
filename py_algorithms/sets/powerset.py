from typing import Any
from typing import List

class PowerSet:
    @staticmethod
    def apply(xs: List[Any]) -> List[Any]: # Any => can contain elements of any data type
        """Takes a list xs as input and returns a list of all possible subsets."""
        result = []

        # A bitwise left shift operation equivalent to 2^len(xs).
        cardinality = 1 << len(xs)
        # This calculates the total number of subsets.
        # If xs = [1, 2, 3] => cardinality = 2^3 = 8 (decimal) subsets in a powerset
        #                   => cardinality = 1 << 3 => shift left 3 times => 1000 (binary)

        i=0
        while i < cardinality: # i = from 0 to cardinality - 1 (2^n - 1)
            # Each i is written in binary and acts as a "mask" to determine which elements are included in a subset.

            stack = []
            for j in range(0, len(xs)): # j represents the position (index) of an element in xs
                if 0 != i & 1 << j: # binary representation
                    stack.append(xs[j])
            result.append(stack)
            i += 1
        return result

        ## i is the row number (from 0 to 7 in decimal)
        # Each bit in i determines whether we include xs[j] in the subset
        # j is the position of each bit in i, mapping to elements in xs.

        # Ex:
        # i = 0b011  (3 in decimal) 
        # j = 0       (checking bit position 0)  
        # -> 0b011 & (1 << 0)  → 0b011 & 0b001  → 1  → include xs[0] (a)
        
        # j = 1       (checking bit position 1)  
        # -> 0b011 & (1 << 1)  → 0b011 & 0b010  → 1  → include xs[1] (b)

        # j = 2       (checking bit position 2)  
        # -> 0b011 & (1 << 2)  → 0b011 & 0b100  → 0  → do not include xs[2] (c)

        # => for i = 3 (0b011), the subset is [a, b].

        #  Expression	  Binary Calculation 	Decimal Result
        # 0b011 & 0b001	   011 & 001 = 001	      1
        # 0b011 & 0b100	   011 & 100 = 000	      0

                    