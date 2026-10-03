class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        length = len(grid)
        width = len(grid[0])
        visited = set()
        max_area = 0

        def dfs(row, col):
            if row < 0 or col < 0 or row >= length or col >= width or (row, col) in visited or grid[row][col] != 1:
                return 0

            visited.add((row, col))
            
            return (1 + dfs(row+1, col) + dfs(row, col+1) + dfs(row-1, col) + dfs(row, col-1))
    
        for r in range(length):
            for c in range(width):
                if (r,c) not in visited and grid[r][c] == 1:
                    print("dfs")
                    max_area = max(max_area, dfs(r, c))
        return max_area


        