class Solution:
    def findMin(self, nums: List[int]) -> int:
        right = len(nums) - 1
        left = 0

        while right > left:
            curr = (right + left)//2
            if nums[curr] > nums[right]:
                left = curr + 1
            else:
                right = curr
            
        return nums[left]