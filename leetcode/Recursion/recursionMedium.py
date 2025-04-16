class MediumSolution(object):
    def Permutations46(self, nums: list[int]) -> list[list[int]]:

        res = []
        def helper(nums, curr_list):
            # base case
            if len(nums) == len(curr_list):
                res.append(curr_list[:])
                return

            for num in nums:
                if num in curr_list:
                    continue
                curr_list.append(num)
                helper(nums, curr_list)
                curr_list.pop()
        helper(nums, [])
        return res

    # Given an array nums of distinct integers, return all the possible permutations. 
    # You can return the answer in any order.

    # Input: nums = [1,2,3]
    # Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    # TC: O(n!) - backtracking, n is the length of nums
    # SC: O(n!) - space for the result list (curr_list shallow copy), n is the length of nums


m = MediumSolution()
sol1 = m.Permutations46([1,2,3])

print(sol1)