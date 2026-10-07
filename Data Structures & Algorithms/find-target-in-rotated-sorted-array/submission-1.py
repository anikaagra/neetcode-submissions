class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right, left = len(nums) - 1, 0
        while right >= left:
            mid = (right + left) // 2
            print(right, left, mid)
            if target == nums[mid]:
                return mid
            
            if nums[mid] <= nums[left]:
                if nums[mid] < target <= nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[right] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
