class Solution:
    def climbStairs(self, n: int) -> int:
        # dp: # of ways to reach step 1
        # depends on dp[i - 1] + dp[i - 2] (space optimized with prev and prev2)

        prev = 1
        prev2 = 1

        for i in range(2, n + 1):
            temp = prev2
            prev2 = prev
            prev += temp

        return prev