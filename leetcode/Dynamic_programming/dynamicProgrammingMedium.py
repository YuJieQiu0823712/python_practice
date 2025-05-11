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
