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


    def maximumSubarray53(self,nums: array) -> int:
        # Kadane's Algorithm:
        # Tracks the current subarray sum. Start with the first element (nums[0]).
        # Tracks the maximum sum encountered. Start with the first element (nums[0]).
        # Iterate through the array (extend the current subarray or start a new subarray)
        # Return the maximum subarray sum found (total_max).
        total_sum = nums[0]
        total_max = nums[0]
        for i in range(1,len(nums)):
            total_sum = max(total_sum + nums[i],nums[i])
            total_max = max(total_max,total_sum)
        return total_max    
    # Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    # Output: 6
    # Explanation: The subarray [4,-1,2,1] has the largest sum 6.
    # TC: O(n)
    # SC: O(1)


    def findAllDuplicatesInAnArray442(self, input: array) -> array:
        # seen = set()
        # ans = []
        # for num in input:
        #     if num in seen:
        #         ans.append(num)
        #     else:
        #         seen.add(num)
        # return ans
        # # TC: O(n)
        # # SC: O(n)

        ### 1 <= input[i] <= n (n=size of array) ###
        # if the numbers are repeated, the (number - 1) = indexes are the same.
        # use Flag => mark every (number - 1)'s corresponding index to be negative.
        # iterate, if the input[idx] is negative, it means we have already seen that one (added to output array)
        output = []
        for i in range(len(input)):
            idx = abs(input[i]) - 1
            if input[idx] < 0:
                output.append(idx + 1)
            input[idx] = -input[idx]
        return output
    # Input: nums = [4,3,2,7,8,2,3,1]
    # Output: [2,3]
    # TC: O(n)
    # SC: O(1)

    
    def rotateMatrix48(self, input: list[list[int]]) -> list[list[int]]:    
        # nested loop => swap
        # reverse each row   
        for row in range(len(input)):
            for col in range(row, len(input)):
                input[row][col], input[col][row] = input[col][row], input[row][col]
        for i in range(len(input)):
            input[i].reverse()
        return input
    # Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    # Output: [[7,4,1],[8,5,2],[9,6,3]]
    # TC: O(n^2)
    # SC: O(1)



    
m = MediumSolution()
sol1 = m.mergeIntervals56([[1,3],[2,6],[8,10],[15,18]])
sol2 = m.bestTimeToBuyAndSellStockII122([7,1,5,3,6,4])
sol3 = m.maximumSubarray53([-2,1,-3,4,-1,2,1,-5,4])
sol4 = m.findAllDuplicatesInAnArray442([4,3,2,7,8,2,3,1])
sol5 = m.rotateMatrix48([[1,2,3],[4,5,6],[7,8,9]])

print(sol1)
print(sol2)
print(sol3)
print(sol4)
print(sol5)
