class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        largest = 0

        for n in nums_set:
            if n - 1 not in nums_set:
                curr = n
                while curr in nums_set:
                    curr += 1
                largest = max(largest, curr-n)

        return largest

                    