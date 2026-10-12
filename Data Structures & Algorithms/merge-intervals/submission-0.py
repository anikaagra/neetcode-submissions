class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output = [intervals[0]]

        for start, end in intervals[1:]:
            curr_end = output[-1][1]
            if start <= curr_end:
                output[-1][1] = max(end, curr_end)
            else:
                output.append([start, end])

        return output