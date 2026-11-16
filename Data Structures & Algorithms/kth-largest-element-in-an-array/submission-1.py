class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # create max heap and pop when larger than k
        # pop k elems and return value
        h = []
        for n in nums:
            heapq.heappush(h, n)
            
            if len(h) > k:
                heapq.heappop(h)

        return h[0]