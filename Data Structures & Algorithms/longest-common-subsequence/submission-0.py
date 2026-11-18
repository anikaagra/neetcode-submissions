class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp[i][j] represents the longest common subsequence for text1[i:] and text2[j:]
        # dp[0][j] = 0 and dp[i][0] = 0
        # dp[i][j] = max(dp[i+1][j], dp[i][j+1]) or dp[i+1][j+1] + 1 if text1[i] = text2[j]
        n = len(text1)
        m = len(text2)

        dp = [[0 for j in range(m + 1)] for i in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        
        return dp[0][0]