class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] = max(dp[i-2] + nums[i], dp[i-1]) 
        # space optimize with prev and prev2 rather than full array

        prev2 = 0
        prev = nums[0]

        for i in range(1, len(nums)):
            curr = max(prev2 + nums[i], prev)
            prev2 = prev
            prev = curr

        return prev