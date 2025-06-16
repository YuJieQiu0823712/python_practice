class MediumSolution:
    def wordBreak139(self, s: str, wordDict: list[str]) -> bool:
        """
        Determines if the input string `s` can be segmented into a sequence of one or more words from `wordDict`.

        Args:
            s (str): The input string to be segmented.
            wordDict (list[str]): A list of valid words.

        Returns:
            bool: True if the string can be segmented using the dictionary, False otherwise.

        Approach:
            - Use dynamic programming.
            - `dp[i]` is True if `s[:i]` can be segmented using words from `wordDict`.
            - Start with dp[0] = True (empty string).
            - For each position i in the string, check if any word in the dictionary matches `s[i:i+len(word)]`
            and if `dp[i]` is True, then mark `dp[i+len(word)]` as True.

        TC: O(n)
        SC: O(n)    
        """
        dp = [False] * (len(s)+1)  # Initialize dp array with False
        dp[0] = True
        for i in range(len(s)):
            if dp[i]:
                for word in wordDict:
                    if s[i:i+len(word)] == word:
                        dp[i+len(word)] = True
        return dp[-1]

    def twoKeysKeyboard650(self, n: int) -> int:
        """
        Calculates the minimum number of operations needed to print exactly `n` 'A's on a notepad
        using two operations: Copy All and Paste.

        Args:
            n (int): The number of 'A's to print.

        Returns:
            int: Minimum number of operations to reach `n` 'A's.

        Approach:
            - Use dynamic programming.
            - `dp[i]` is the minimum number of steps to get i 'A's.
            - Initialize dp[i] = i (worst case: paste one 'A' at a time).
            - For each number i from 2 to n, iterate backwards through its divisors.
            If `i` is divisible by `j`, set `dp[i] = dp[j] + i // j`:
                - dp[j] to build up to j 'A's,
                - one "Copy All" and `i // j - 1` "Paste" operations.

        TC: O(n^2)
        SC: O(n)  
        """
        dp = [i for i in range(n+1)]
        dp[1] = 0

        for curr_n in range(2,n+1):
            for curr_chars_can_be_copied_and_pasted in range(curr_n//2, 1, -1):
                if curr_n % curr_chars_can_be_copied_and_pasted == 0:
                    dp[curr_n] = dp[curr_chars_can_be_copied_and_pasted] + curr_n//curr_chars_can_be_copied_and_pasted
                    break
        return dp[n]

    def maximumNumberOfPointsWithCost1937(self, points: list[list[int]]) -> int:
        
        """
        Given a 2D list `points`, where `points[i][j]` represents the points you can earn at row `i`, column `j`,
        computes the maximum number of points that can be obtained by selecting one cell from each row.
        The constraint is that moving from column `j` in row `i-1` to column `k` in row `i` costs `abs(j - k)` points.

        Args:
            points (list[list[int]]): A 2D grid of integers representing points per cell.

        Returns:
            int: The maximum number of points achievable from top to bottom row, selecting one cell per row,
                and subtracting the movement cost between columns.

        Approach:
            - Use dynamic programming where `dp[col]` stores the max points achievable at column `col` of the current row.
            - Initialize `dp` with the first row.
            - For each subsequent row:
                1. First sweep left to right to consider optimal transitions subtracting 1 per step.
                2. Then sweep right to left to catch optimal transitions missed in the first pass.
                3. Update `dp[col] = points[row][col] + max achievable from previous row (after cost)`.
            - The final answer is the max value in the last dp array.

        TC: O(n^2)
        SC: O(n)  
        """
        rows = len(points)
        cols = len(points[0])
        dp = points[0]

        for row in range(1, rows):
            for col in range(1, cols):
                dp[col] = max(dp[col-1] - 1, dp[col])
            for col in range(cols-2, -1, -1):
                dp[col] = max(dp[col+1] - 1, dp[col])
            dp = [points[row][col] + dp[col] for col in range(cols)]
        return max(dp)


