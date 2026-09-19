from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_by_num = defaultdict(int)
        for num in nums:
            count_by_num[num] += 1
        
        count_by_freq = [[] for i in range(len(nums) + 1)]
        for num, count in count_by_num.items():
            count_by_freq[count].append(num)
        
        res = []
        for i in range(len(count_by_freq) - 1, 0, -1):
            for num in count_by_freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
