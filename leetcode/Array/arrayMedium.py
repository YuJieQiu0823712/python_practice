import array

class MediumSolution(object):
    """
    A class used to represent medium level solutions.
    """

    def mergeIntervals56(self, input: array) -> array:
        # Sort the intervals
        # Iterate through the list
        # Check for overlap
        # Merge overlapping intervals (.pop() the overlapped one)
        # Move forward when no overlap
        # Return the modified input list
        input.sort() # modifies the original list
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
    # TC: O(n log n) => Sorting a list of length n takes O(n log n) time.
    # SC: O(1) => in-place sorting


    def bestTimeToBuyAndSellStockII122(self, prices:array) -> int:
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
                i+=1
        return profit
    # Input: prices = [7,1,5,3,6,4]
    # Output: 7
    # Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
    # Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
    # Total profit is 4 + 3 = 7.
    # TC: O(n)
    # SC: O(1)
    
m = MediumSolution()
sol1 = m.mergeIntervals56([[1,3],[2,6],[8,10],[15,18]])
sol2 = m.bestTimeToBuyAndSellStockII122([7,1,5,3,6,4])

print(sol1)
print(sol2)
