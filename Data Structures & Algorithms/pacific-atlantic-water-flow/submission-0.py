class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        pacific = set()
        atlantic = set()
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def dfs(r, c, visited): 
            visited.add((r,c))
            for dr, dc in directions:
                nr = r+dr
                nc = c+dc
                if nr >= 0 and nc >= 0 and nr < n and nc < m and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, visited)

        # pacific ocean touches [i, 0], [0, j] where i: 0, n-1 and j: 0, m-1
        # atlantic ocean touches [i, m-1], [n-1, j] where i: 0, n-1 and j: 0, m-1

        for r in range(n):
            dfs(r, 0, pacific)
            dfs(r, m-1, atlantic)
        for c in range(m):
            dfs(0, c, pacific)
            dfs(n-1, c, atlantic)

        return [[r, c] for r, c in pacific & atlantic]