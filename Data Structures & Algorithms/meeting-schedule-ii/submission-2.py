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
        greedy:
            track how number of active meetings changes over time
            max reached is number of rooms needed
            store events (start, +1) and (end, -1)
            sort by time, break ties by processing end before start
            add event to ongoing count
            update out to max
        '''
        time = []
        count = 0
        out = 0

        for interval in intervals:
            time.append((interval.start, 1))
            time.append((interval.end, -1))

        time.sort(key=lambda x: (x[0], x[1]))

        for t in time:
            count += t[1]
            out = max(out, count)
        
        return out
