class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # lis[i] represents the length of the longest increasing subsequence from i (i <= n)
        # if nums[i] < nums[j] for j where i left off (lis[i+1:])
        n = len(nums)
        lis = [1] * n

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    lis[i] = max(lis[i], lis[j] + 1)
        
        return max(lis)