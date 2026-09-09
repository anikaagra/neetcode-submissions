class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        char_index = {}
        for i,n in enumerate(nums):
            remainder = target - n
            if n in char_index:
                return [char_index[n], i]
            else:
                char_index[remainder] = i
        
