class MediumSolution:
    def wordBreak139(self, s: str, wordDict: list[str]) -> bool:
        dp = [False] * (len(s)+1)  # Initialize dp array with False
        dp[0] = True
        for i in range(len(s)):
            if dp[i]:
                for word in wordDict:
                    if s[i:i+len(word)] == word:
                        dp[i+len(word)] = True
        return dp[-1]

    def twoKeysKeyboard650(self, n: int) -> int:
        dp = [i for i in range(n+1)]
        dp[1] = 0

        for curr_n in range(2,n+1):
            for curr_chars_can_be_copied_and_pasted in range(curr_n//2, 1, -1):
                if curr_n % curr_chars_can_be_copied_and_pasted == 0:
                    dp[curr_n] = dp[curr_chars_can_be_copied_and_pasted] + curr_n//curr_chars_can_be_copied_and_pasted
                    break
        return dp[n]

