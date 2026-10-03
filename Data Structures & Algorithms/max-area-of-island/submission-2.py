class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        length = len(grid)
        width = len(grid[0])
        direction = [[1, 0], [0, 1], [0, -1], [-1, 0]]
        max_area = 0

        def dfs(row, col):
            if row < 0 or col < 0 or row >= length or col >= width or grid[row][col] != 1:
                return 0

            grid[row][col] = 0
            curr_count = 1

            for dr, dc in direction:
                curr_count += dfs(row + dr, col + dc)
            
            return curr_count
    
        for r in range(length):
            for c in range(width):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
        return max_area


        