from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        sorted_by_count = []
        for num, val in count.items():
            heapq.heappush(sorted_by_count, (val, num))
            if len(sorted_by_count) > k:
                heapq.heappop(sorted_by_count)

        return [num for val, num in sorted_by_count]