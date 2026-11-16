from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count freqs for each elem
        # create min heap, ordered by freq, and pop when > k 
        # pop remaining and append to output

        freqs = defaultdict(int)
        for n in nums:
            freqs[n] += 1
        
        h = []
        for n in freqs.keys():
            heapq.heappush(h, (freqs[n], n))
            if len(h) > k:
                heapq.heappop(h)
        
        out = []
        for i in range(k):
            out.append(heapq.heappop(h)[1])
        
        return out
