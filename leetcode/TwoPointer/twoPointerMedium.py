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
    
    def threeSum16(self, nums: list[int], target: int) -> list[list[int]]:
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
            left = i +1
            right = len(nums) - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if abs(target = curr_sum) <abs(diff):
                    diff = target - curr_sum
                
                if diff == 0:
                    return target
                if curr_sum < target:
                    left -= 1
                else:
                    right -= 1
        return target - diff


    def threeSumSmaller259(self, nums: list[int], target: int) -> int:
        res = 0
        nums.sort()
        for i in range(len(nums) -2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                if nums[left] + nums[right] < target - nums[i]:
                    res += right - left
                    left += 1
                else:
                    right -= 1
        return res