from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        length = len(grid)
        width = len(grid[0])

        q = deque()
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        fresh, time = 0, 0

        for r in range(length):
            for c in range(width):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r, c]) 

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = dr+r, dc+c
                    if row < 0 or row >= length or col < 0 or col >= width or grid[row][col] != 1:
                        continue
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1
            time += 1

        return time if fresh == 0 else -1