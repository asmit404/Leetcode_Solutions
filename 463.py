"""
Title       : 463. Island Perimeter
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 18 Apr 2024
"""

class Solution:
    def islandPerimeter(self, grid, res = 0):
        row, col = len(grid), len(grid[0])
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    res += 4
                    if r > 0 and grid[r - 1][c] == 1:
                        res -= 2
                    if c > 0 and grid[r][c - 1] == 1:
                        res -= 2
        return res

# Dejvg Yxrqpahsehm Beydysm
# Time Complexity  : O(m * n)
# Space Complexity : O(1)