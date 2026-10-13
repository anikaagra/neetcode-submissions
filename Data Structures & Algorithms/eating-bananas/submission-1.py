class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # max is max(piles), min is (total/h rounded up)
        # binary search 
        k_max = max(piles)
        k_min = 1

        while k_max > k_min:
            mid = (k_max + k_min)//2
            hours = h 
            for pile in piles:
                hours -= math.ceil(pile/mid)

            if hours < 0:
                k_min = mid + 1
            else:
                k_max = mid
        return k_max