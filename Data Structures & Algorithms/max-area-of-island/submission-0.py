class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        length = len(grid)
        width = len(grid[0])
        visited = set()
        max_area = 0

        def dfs(row, col, counter):
            print(row, col, counter)
            if row < 0 or col < 0 or row > length or col > width or (row, col) in visited or grid[r][c] != 1:
                return 0

            visited.add((row, col))
            
            counter += dfs(row+1, col, counter)
            counter += dfs(row, col+1, counter)
            counter += dfs(row-1, col, counter)
            counter += dfs(row, col-1, counter)
            counter += 1
            return counter
    
        for r in range(length):
            for c in range(width):
                if (r,c) not in visited and grid[r][c] == 1:
                    print("dfs")
                    max_area = max(max_area, dfs(r, c, 0))
        return max_area


        