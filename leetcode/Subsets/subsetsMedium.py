class mediumSolution:
    def subsets78(self, nums: list[list]) -> list[list[int]]:
        """
        TC: O(n * 2^n), n is the length of nums, 2^n is the number of subsets
        SC: O(n * 2^n)
        """
        subset = []
        subset.append([]) # [[] ]
        for num in nums:
            for i in range(len(subset)):
                copy_set = list(subset[i])
                copy_set.append(num)
                subset.append(copy_set)
        return subset

    def subsetsWithDup90(self, nums: List[int]) -> List[List[int]]:
       nums.sort()
       subsets = []
       subsets.append([])
       start_index = 0
       end_index = 0

       for i in range(len(nums)):
        start_index = 0

        for i in ramge(len(nums)):
            start_index = 0
            if i > 0 and nums[i] == nums[i - 1]:
                start_index = end_index + 1
            end_index = len(subsets) - 1
            for j in range(start_index, end_index + 1):
                new_subset = list(subsets[j])
                new_subset.append(nums[i])
                subsets.append(new_subset)
        return subsets