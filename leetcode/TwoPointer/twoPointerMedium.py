import math

class MediumSolution:
    def twoSumIIInputArrayIsSorted167(self, numbers:list[int], target: int) -> list[int]:
        """
        Finds two numbers in a sorted array that add up to a specific target.

        Given a 1-indexed array of integers `numbers` that is already sorted in
        non-decreasing order, returns the indices of the two numbers such that 
        they add up to the target.

        Args:
            numbers (List[int]): A list of integers sorted in ascending order.
            target (int): The target sum to find.

        Returns:
            List[int]: A list containing the 1-based indices of the two numbers 
                       that add up to the target. Returns [-1, -1] if no such pair exists.

        """
        point_a = 0
        point_b = len(numbers) - 1

        while point_a < point_b:
            curr_num = numbers[point_a] + numbers[point_b]
            
            if curr_num == target:
                return [point_a +1, point_b + 1]
            if curr_num < target:
                point_a += 1
            else:
                point_b -= 1
        return [-1, -1]


    def threeSum15(self, nums: list[int]) -> list[list[int]]:
        """
        Finds all unique triplets in the array that sum up to zero.

        Args:
            nums (List[int]): A list of integers.

        Returns:
            List[List[int]]: A list of lists, where each inner list contains three integers
                             that sum to zero. The result does not contain duplicate triplets.

        TC: O(n log n) + O(n^2) = O(n^2)
        SC: O(n), because python sort needs use space of N                   
        """
        res = []
        length = len(nums)
        nums.sort() #O(n log n)

        for i in range(length - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = length - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i],nums[left],nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
        return res
    
    def threeSumClosest16(self, nums: list[int], target: int) -> list[list[int]]:
        """
        Finds the sum of three integers in the list `nums` such that the sum is closest to the given `target`.
        
        This implementation sorts the list and uses a two-pointer approach to efficiently find the 
        closest possible sum of any three numbers in the list.

        Args:
            nums (List[int]): A list of integers.
            target (int): The target sum to approach.

        Returns:
            int: The sum of the triplet that is closest to the target.

        TC: O(n^2)
        SC: O(n)    
        """
        nums.sort()
        diff = math.inf

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if abs(target - curr_sum) < abs(diff):
                    diff = target - curr_sum
                
                if diff == 0:
                    return target
                if curr_sum < target:
                    left += 1
                else:
                    right -= 1
        return target - diff


    def threeSumSmaller259(self,nums: list[int], target: int) -> int:
        """
        Counts the number of triplets (i, j, k) such that i < j < k and nums[i] + nums[j] + nums[k] < target.
        The function first sorts the input list and then uses a two-pointer approach to find all valid triplets efficiently.
        
        Args:
            nums (list[int]): A list of integers.
            target (int): The target sum to compare against.

        Returns:
            int: The count of triplets whose sum is less than the target.

        TC: O(n^2)
        SC: O(n)  
        """
        res = 0
        nums.sort() # TC:O(n log n)
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] < target:
                    res += right - left
                    left += 1
                else: 
                    right -= 1
        return res 

    def SubarrayProductLessThanK713(self, nums: list[int], target: int) -> int:
        """
        Returns the number of contiguous subarrays where the product of all elements is less than target.

        Args:
            nums (List[int]): A list of positive integers.
            target (int): The product threshold.

        Returns:
            int: The number of contiguous subarrays with product less than target.

        TC: O(n)
        SC: O(1) 
        """
        left = 0
        count = 0
        product = 1

        for right in range(len(nums)):
            product *= nums[right]
            while product >= target and left <= right:
                product /= nums[left]
                left += 1
            count += right - left + 1
        return count

    
    def sortNumbers75(self, nums: list[int]) -> None:
        """
        Sorts a list of integers containing only 0s, 1s, and 2s in-place 
        such that all 0s come first, followed by 1s, then 2s.

        Args:
            nums (List[int]): A list of integers where each element is 0, 1, or 2.
        
        Returns:
            None
        
        TC: O(n)
        SC: O(1)
        """
        i = 0
        left = 0
        right = len(nums) - 1
        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                i += 1
                left += 1
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
            else:
                i += 1
        return nums

    def fourSum18(self, nums: list[int], target: int) -> list[list[int]]:
        """
        Finds all unique quadruplets in the array that sum up to a specific target.

        Args:
            nums (List[int]): A list of integers.
            target (int): The target sum to find.

        Returns:
            List[List[int]]: A list of lists, where each inner list contains four integers
                             that sum to the target. The result does not contain duplicate quadruplets.

        TC: O(n^3)
        SC: O(n) 
        """
        nums.sort() # O(n log n)
        res = []
        length = len(nums)

        # edge check
        if length < 4:
            return []

        for i in range(length - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, length - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = length - 1
                
                while left < right:
                    curr_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if curr_sum < target:
                        left += 1
                    elif curr_sum > target:
                        right -= 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
        return res

    def shortestUnsortedContinuousSubarray581(self,nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1
        subarr_min = float('inf')
        subarr_max = float('-inf')

        while left < right and nums[left] < nums[left + 1]:
            left += 1
        if left == right:
            return 0
        while right > left and nums[right] > nums[right - 1]:
            right -= 1
        for i in range(left, right + 1):
            subarr_min = min(subarr_min, nums[left])
            subarr_max = max(subarr_max, nums[right])
        while left > 0 and nums[left - 1] > subarr_min:
            left -= 1
        while right < len(nums) - 1 and nums[right + 1] < subarr_max:
            right += 1
        return right  - left + 1
