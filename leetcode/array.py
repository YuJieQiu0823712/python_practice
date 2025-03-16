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
        # find which one earn the largest and keep that
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


    def twoSum1(self, nums: array, target: int) -> array:
        # We use a "Hash Map" to store numbers we have seen so far along with their indices.
        # For each number in the array, we calculate its complement "target - current_number".
        # If the complement exists in our map, we return the indices of both numbers.
        # Otherwise, we store the current number along with its index in the map.
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement],i]
            numMap[nums[i]] = i
        return [] # No solution found
    # Input: nums=[3,2,4]
    #        target=6
    # Output: [1,2] => Because nums[1] + nums[2] == 6
    # TC: O(n^2) 
    # SC: O(n)


e = EasySolution()
sol1 = e.duplicateZeros1089([1,0,2,3,0,4,5,0]) 
sol2 = e.mergSortedArray88([1,2,3,0,0,0],[2,5,6])
sol3 = e.removeElement27([0,1,2,2,3,0,4,2],2)
sol4 = e.removeDuplicatesFromSortedArray26([0,0,1,1,1,2,2,3,3,4])
sol5 = e.checkIfNAndItsDoubleExist1346([10,2,5,3])
sol6 = e.BestTimeToBuyAndSellStock121([7,1,5,3,6,4])
sol = e.twoSum1([3,2,4],6)



print(sol1)
print(sol2)
print(sol3)
print(sol4)
print(sol5)
print(sol6)
print(sol)


