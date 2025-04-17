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


    def combinationSum(self, candidate: list[int], target: int) -> list[list[int]]:
        self.res = []
        def backtracking(candicate, temp_list, remainder, index):
            # base case
            if remainder == 0:
                self.res.append(temp_list[:]) # shallow copy, otherwise the temp_list will be modified
                return
            if remainder < 0:
                return
            for i in range(index,len(candicate)): # previous candidates are not re-selected, avoiding permutations
                temp_list.append(candidate[i])
                backtracking(candidate, temp_list, remainder - candidate[i], i)
                temp_list.pop()
        backtracking(candidate, [], target, 0)
        return self.res     

  
    # Input: candidates = [2,3,6,7], target = 7
    # Output: [[2,2,3],[7]]
    # Explanation:
    # 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
    # 7 is a candidate, and 7 = 7.
    # These are the only two combinations. 

m = MediumSolution()
sol1 = m.Permutations46([1,2,3])
sol2 = m.combinationSum([2,3,6,7], 7)

print(sol1)
print(sol2)