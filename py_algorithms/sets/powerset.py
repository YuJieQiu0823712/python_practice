

class Powerset:
    @staticmethod
    def apply(xs: List[Any]) -> List[Any]: # Any => can contain elements of any data type
        """Takes a list xs as input and returns a list of all possible subsets."""
        result = []

        # A bitwise left shift operation equivalent to 2^len(xs).
        cadinality = 1 << len(xs)
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

                    