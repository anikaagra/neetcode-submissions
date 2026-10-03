class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0
        visited = set()

        length = len(grid)
        width = len(grid[0])

        def dfs(row, col):
            if row >= length or col >= width or row < 0 or col < 0:
                return 
            if (row, col) in visited:
                return 
            if grid[row][col] == "0":
                return
            
            visited.add((row, col))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)


        for r in range(length):
            for c in range(width):
                if (r, c) not in visited and grid[r][c] == "1":
                    dfs(r, c)
                    counter += 1

        return counter