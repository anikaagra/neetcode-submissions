"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        ''' 
        min heap:
            sort by start time
            store end times in heap
            if earliest end time is <= current start, pop top
            otherwise allocate new room
        '''
        h = []
        intervals.sort(key=lambda x: x.start)
      
        for interval in intervals:
            if h and h[0] <= interval.start:
                heapq.heappop(h)
            heapq.heappush(h, interval.end)

        return len(h)
