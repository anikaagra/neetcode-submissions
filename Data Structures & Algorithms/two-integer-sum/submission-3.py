class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        to_index = {}

        for i, n in enumerate(nums):
            if target - n in to_index:
                return [to_index[target - n], i]
            to_index[n] = i