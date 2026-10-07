class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def findDist(x1, y1):
            return (x1)**2 + (y1)**2

        distHeap = []
        for x,y in points:
            dist = -findDist(x,y)
            heapq.heappush(distHeap, [dist, x, y])
            if len(distHeap) > k:
                heapq.heappop(distHeap)
        
        output = []
        while distHeap:
            dist, x, y = heapq.heappop(distHeap)
            output.append([x, y])
        return output