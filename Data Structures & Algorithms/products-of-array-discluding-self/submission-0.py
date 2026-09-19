class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # with division  

        zeros = 0
        total = 1
        for n in nums:
            if n == 0:
                zeros += 1
            else:
                total *= n

        res = [0]*len(nums)
        if zeros == 0:
            for i, n in enumerate(nums):
                res[i] = (total//n)
        elif zeros == 1:
            for i, n in enumerate(nums):
                if n == 0:
                    res[i] = total

        return res 
        