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