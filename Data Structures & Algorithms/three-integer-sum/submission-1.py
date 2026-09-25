class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        output = []

        for static in range(len(nums) - 2):
            if static > 0 and nums[static] == nums[static-1]:
                continue
            
            left = static + 1
            right = len(nums) - 1

            while right > left:
                curr_sum = nums[left] + nums[right] + nums[static]
                if curr_sum > 0:
                    right -= 1
                    
                if curr_sum < 0:
                    left += 1
                    
                if curr_sum == 0:
                    output.append([nums[left], nums[right], nums[static]])
                    right -= 1
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return output