class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)
        def findDist(x):
            return (x[0])**2 + (x[1])**2

        def partition(l, r):
            pivot = r
            pt = points[pivot]
            pivot_dist = findDist(pt)
            i = l
            for j in range(l, r):
                if findDist(points[j]) < pivot_dist:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            points[i], points[r] = points[r], points[i]
            return i

        L = 0
        R = n - 1
        pivot = n

        while pivot != k:
            pivot = partition(L, R)
            if pivot < k:
                L = pivot + 1
            elif pivot > k:
                R = pivot - 1
        return points[:k]