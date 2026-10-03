class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        length = len(grid)
        width = len(grid[0])
        visited = set()
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def dfs(r, c):
            if r < 0 or c < 0 or r >= length or c >= width or (r, c) in visited or grid[r][c] != 1:
                return 0
            print(visited)
            visited.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            return 1

        # minutes = 0
        # for r in range(length):
        #     for c in range(width):
        #         if (r, c) not in visited and grid[r][c] == 2:
        #             print(f"dfs {r, c, minutes}")
        #             minutes += dfs(r,c)
        dfs(2, 2)
       # return minutes