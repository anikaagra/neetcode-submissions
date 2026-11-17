"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from collections import defaultdict

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        ''' 
        sweep line:
            number of rooms is the number of meetings at once
            store mp[start] and mp[end]
            track ongoing meetings and max across all times in mp
        '''
        mp = defaultdict(int)
        for interval in intervals:
            start = interval.start
            end = interval.end
            mp[start] += 1
            mp[end] -= 1
        
        prev = 0
        res = 0
        for i in sorted(mp.keys()):
            prev += mp[i]
            res = max(res, prev)

        return res

