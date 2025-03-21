import array

class EasySolution(object):
    """
    A class used to represent easy level solutions.
    """
    def duplicateZeros1089(self, arr: array) -> array:
        i=0
        while i < len(arr):
            if arr[i] != 0:
                i += 1
            else:
                arr.insert(i+1, 0) # (index,value)
                arr.pop() # pop last index
                i += 2
        return arr
    # Input: [1,0,2,3,0,4,5,0]
    # Output: [1,0,0,2,3,0,0,4]
    # TC: O(n) => O(n)+O(m)+O(1) => n is length of input, m is the position we want to insert
    # SC: O(1) We did inplace modification, no extra space.

   
    def mergSortedArray88(self, num1: array, num2: array) -> array:
        # compare A to B 
        # if A>B => A put in C
        # else => B put in C
        # (pointer start from the last: ptr_a->num1 last / ptr_b->num2 last / ptr_c->last)
        # pointer-=1

        m = len(num1) - len(num2)
        n = len(num2)
  
        ptr_a = m-1
        ptr_b = n-1
        last = m+n-1

        while ptr_a>=0 and ptr_b>=0:
            if num1[ptr_a] > num2[ptr_b]:
                num1[last] = num1[ptr_a]
                ptr_a-=1
                last-=1
            else:
                num1[last] = num2[ptr_b]
                ptr_b-=1
                last-=1
        
        
        while ptr_b>=0:
            num1[last] = num2[ptr_b]
            ptr_b-=1
            last-=1

        return num1  
    # Input: num1=[1,2,3,0,0,0]
    #        num2=[2,5,6]
    # Output: [1,2,2,3,5,6]
    # TC: O(n) => O(m)+O(n) => m is length of num1, n is length of num2
    # SC: O(1) We did inplace modification, no extra space.


    def removeElement27(self, nums: array, val: int) -> int:
        # strategy: not remove the val, instead iterate the array and not add val
        ptr = 0
        for num in nums:
            if num != val:
                nums[ptr] = num
                ptr += 1
        return ptr
    # Input: nums=[0,1,2,2,3,0,4,2]
    #        val=2
    # Output: 5 => Because nums = [0,1,3,0,4]
    # TC: O(n), n is length nums
    # SC: O(1), no extra memory


    def removeDuplicatesFromSortedArray26(self, nums: array):
        pre = None
        ptr = 0
        for num in nums:
            if num != pre:
                pre = num
                nums[ptr] = num
                ptr +=1
        return ptr
    # Input: nums=[0,0,1,1,1,2,2,3,3,4]
    # Output: 5 => Because nums = [0,1,2,3,4]
    # TC: O(n)
    # SC: O(1)

    def checkIfNAndItsDoubleExist1346(self, nums: array) -> bool:
        # First index i multiply or divide by index j
        # If this result is in the set(), then return True
        # Otherwise, add this result to set()
        seen = set()
        for num in nums:
            if (num * 2) in seen or (num / 2) in seen:
                return True
            else:
                seen.add(num)
        return False
    # Input: nums=[10,2,5,3]
    # Output: True => Because nums[0] == 10 == 2 * 5 == 2 * arr[2]
    # TC: O(n), n is length of array
    # SC: O(n), n is the length of set

    def BestTimeToBuyAndSellStock121(self, input: array) -> int:
        # Renew the minimum price and keep which one earns the largest profit
        min_price = float('inf')
        max_profit = 0
        for price in input:
            min_price = min(price, min_price)
            max_profit = max(price-min_price, max_profit)
        return max_profit
    # Input: nums=[7,1,5,3,6,4]
    # Output: 5 => Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    # TC: O(n)
    # SC: O(1)

    def ReplaceElementsWithGreatestElementsOnRightSide1299(self, input: array) -> array:
        # 1. Initialize current_max: 
        #   Start from the last element, which has no elements to its right. 
        #   Set it to -1 and store its original value as current_max.
        # 2. Traverse the array in reverse:
        #   For each element, update it to current_max (the greatest element seen so far on its right).
        # 3. Update current_max:
        #   Compare the original value of the current element with current_max and update current_max if necessary.
        max_seen = 0
        current_max = input[-1]
        input[-1] = -1
        for i in range(len(input)-2, -1, -1):
            max_seen = max(input[i], current_max)
            input[i] = current_max
            current_max = max_seen
        return input
    # Input: arr = [17,18,5,4,6,1]
    # Output: [18,6,6,6,1,-1]
    # Explanation: 
    # - index 0 --> the greatest element to the right of index 0 is index 1 (18).
    # - index 1 --> the greatest element to the right of index 1 is index 4 (6).
    # - index 2 --> the greatest element to the right of index 2 is index 4 (6).
    # - index 3 --> the greatest element to the right of index 3 is index 4 (6).
    # - index 4 --> the greatest element to the right of index 4 is index 5 (1).
    # - index 5 --> there are no elements to the right of index 5, so we put -1.
    # TC: O(n)
    # SC: O(1)


    def sortArrayByParity905(self, input: array) -> array:
        # if the current value is an even number, then swap its position with the indicator.
        if not input:
            return []
        ptr=0
        for i in range(len(input)):
            if input[i] %2 == 0:
                input[ptr], input[i] = input[i], input[ptr]
                ptr += 1
        return input
    # Input: arr = [3,1,2,4]
    # Output: [2,4,3,1]
    # TC: O(n)
    # SC: O(1)


    def squaresOfASortedArray977(self,input: array) -> array:
        # square the value in the position of the left pointer
        # square the value in the position of the right pointer
        # compare the value which one is larger then add it to a new list
        # iterate the input array
        left_ptr = 0
        right_ptr = len(input) - 1
        newArray = []
        while left_ptr <= right_ptr:
            if input[left_ptr]**2 > input[right_ptr]**2:
                newArray.append(input[left_ptr]**2)
                left_ptr += 1
            else:
                newArray.append(input[right_ptr]**2)
                right_ptr -= 1
        reversed_Array = reversed(newArray)        
        return list(reversed_Array)
    # Input: nums = [-4,-1,0,3,10]
    # Output: [0,1,9,16,100]
    # TC: O(n)
    # SC: O(n)


    def highestChecker1051(self, input: array) -> int:
        sorted_input = sorted(input)
        count = 0
        for i in range(len(input)):
            if sorted_input[i] != input[i]:
                count += 1
        return count

    # Input: heights = [1,1,4,2,1,3]
    # Output: 3
    # Explanation: 
    # heights:  [1,1,4,2,1,3]
    # expected: [1,1,1,2,3,4]
    # Indices 2, 4, and 5 do not match.
    # TC: O(n log n) => Sorting a list of length n takes O(n log n) time.
    # SC: O(n) => The sorted() function creates a new sorted list, requiring O(n) additional space.




e = EasySolution()
sol1 = e.duplicateZeros1089([1,0,2,3,0,4,5,0]) 
sol2 = e.mergSortedArray88([1,2,3,0,0,0],[2,5,6])
sol3 = e.removeElement27([0,1,2,2,3,0,4,2],2)
sol4 = e.removeDuplicatesFromSortedArray26([0,0,1,1,1,2,2,3,3,4])
sol5 = e.checkIfNAndItsDoubleExist1346([10,2,5,3])
sol6 = e.BestTimeToBuyAndSellStock121([7,1,5,3,6,4])
sol7 = e.ReplaceElementsWithGreatestElementsOnRightSide1299([17,18,5,4,6,1])
sol8 = e.sortArrayByParity905([3,1,2,4])
sol9 = e.squaresOfASortedArray977([-4,-1,0,3,10])
sol10 = e.highestChecker1051([1,1,4,2,1,3])



print(sol1)
print(sol2)
print(sol3)
print(sol4)
print(sol5)
print(sol6)
print(sol7)
print(sol8)
print(sol9)
print(sol10)



