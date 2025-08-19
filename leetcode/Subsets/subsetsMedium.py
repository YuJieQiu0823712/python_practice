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

    def subsetsWithDup90(self, nums: list[int]) -> list[list[int]]:
        """
        TC: O(n * 2^n), n is the length of nums, 2^n is the number of subsets
        SC: O(n * 2^n)
        """
        nums.sort() # n log n
        subsets = []
        subsets.append([])
        start_index = 0
        end_index = 0

        for i in range(len(nums)):
            start_index = 0
            if i > 0 and nums[i] == nums[i - 1]:
                start_index = end_index + 1
            end_index = len(subsets) - 1
            for j in range(start_index, end_index + 1):
                new_subset = list(subsets[j])
                new_subset.append(nums[i])
                subsets.append(new_subset)
        return subsets

    def letterCasePermutation784(self, s: str) -> list[str]:
        """
        TC: O(n * 2^n), n is the length of s, 2^n is the number of permutation
        SC: O(n * 2^n)
        """
        permutation = []
        permutation.append(s)
        for i in range(len(s)):
            if s[i].isalpha():
                for j in range(len(permutation)):
                    chars = list(permutation[j])
                    chars[i] = chars[i].swapcase() #
                    permutation.append("".join(chars))
        return permutation

    
    def generateParentheses22(self, n: int) -> list[str]:
        """
        TC: O(n!)
        SC: O(n!)
        """
        res = []

        def backtrack(s, left, right):
            if len(s) == n * 2: # n*2 is the length of valid parentheses
                res.append(s)
            else:
                if left > right:
                    backtrack(s + ")", left, right + 1)
                if left < n:
                    backtrack(s + "(", left + 1, right)
        backtrack("", 0, 0)
        return res


