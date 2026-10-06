class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Alg: BFS to find shortest distance
        n = len(grid)
        m = len(grid[0])
        INF = 2147483647 
        q = deque()
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 0:
                    q.append((r, c))

        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if nr >= 0 and nc >= 0 and nr < n and nc < m and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))
