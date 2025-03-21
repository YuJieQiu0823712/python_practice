import array

class MediumSolution(object):
    """
    A class used to represent medium level solutions.
    """

    def mergeIntervals56(self, input: array) -> array:
        input.sort()
        i=1
        while i < len(input):
            if input[i-1][1] >= input[i][0]:
                input[i-1][1] = max(input[i-1][1],input[i][1])
                input.pop(i)
            else:
                i+=1
        return input
    # Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    # Output: [[1,6],[8,10],[15,18]]
    # Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
    
m = MediumSolution()
sol1 = m.mergeIntervals56([[1,3],[2,6],[8,10],[15,18]])

print(sol1)

