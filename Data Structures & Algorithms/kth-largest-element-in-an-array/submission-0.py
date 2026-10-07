class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # use max heap and pop elems if > k. pop once more to get kth largest elem
        h = []
        for n in nums:
            heapq.heappush(h, -n)
        for i in range(k-1):
            heapq.heappop(h)
        return -(heapq.heappop(h))
