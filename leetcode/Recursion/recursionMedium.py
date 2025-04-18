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


    def combinationSum39(self, candidate: list[int], target: int) -> list[list[int]]:
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

    def maxAreaOfIsland695(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0
        size = 0
        max_island = 0
        row_len = len(grid)
        col_len = len(grid[0])
        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == 1:
                    island_size = self.count_island_size(grid, row, col, 1)
                    max_island = max(max_island, island_size)
        return max_island
    def count_island_size(self, grid, row, col, size):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != 1:
            return 0
        grid[row][col] = 0 # mark as visited
        directions = [(row-1, col), (row+1, col), (row, col-1),(row, col+1)]
        for r,c in directions:
            size += self.count_island_size(grid, r, c, 1)
        return size

    # You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
    # You may assume all four edges of the grid are surrounded by water.
    # The area of an island is the number of cells with a value 1 in the island.
    # Return the maximum area of an island in grid. If there is no island, return 0.

    # Input: grid = 
    # [[0,0,1,0,0,0,0,1,0,0,0,0,0],
    # [0,0,0,0,0,0,0,1,1,1,0,0,0],
    # [0,1,1,0,1,0,0,0,0,0,0,0,0],
    # [0,1,0,0,1,1,0,0,1,0,1,0,0],
    # [0,1,0,0,1,1,0,0,1,1,1,0,0],
    # [0,0,0,0,0,0,0,0,0,0,1,0,0],
    # [0,0,0,0,0,0,0,1,1,1,0,0,0],
    # [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    # Output: 6
    # Explanation: The answer is not 11, because the island must be connected 4-directionally.
    
    # TC: O(R*C) - R is the number of rows, C is the number of columns
    # SC: O(R*C) - space for the grid (visited) and recursion stack

m = MediumSolution()
sol1 = m.Permutations46([1,2,3])
sol2 = m.combinationSum39([2,3,6,7], 7)
sol3 = m.maxAreaOfIsland695([[0,0,1,0,0,0,0,1,0,0,0,0,0],
                            [0,0,0,0,0,0,0,1,1,1,0,0,0],
                            [0,1,1,0,1,0,0,0,0,0,0,0,0],
                            [0,1,0,0,1,1,0,0,1,0,1,0,0],
                            [0,1,0,0,1,1,0,0,1,1,1,0,0],
                            [0,0,0,0,0,0,0,0,0,0,1,0,0],
                            [0,0,0,0,0,0,0,1,1,1,0,0,0],
                            [0,0,0,0,0,0,0,1,1,0,0,0,0]])   

print(sol1)
print(sol2)
print(sol3)