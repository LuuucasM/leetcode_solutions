class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        val_grid = [[0 for _ in grid[0]] for _ in grid]

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if row == 0 and col == 0:
                    val_grid[row][col] = grid[row][col]
                elif row == 0:
                    val_grid[row][col] = val_grid[row][col-1] + grid[row][col]
                elif col == 0:
                    val_grid[row][col] = val_grid[row-1][col] + grid[row][col]
                else:
                    val_grid[row][col] = min(val_grid[row-1][col], val_grid[row][col-1]) + grid[row][col]
        return val_grid[-1][-1]