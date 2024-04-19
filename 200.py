"""
Title       : 200. Number of Islands
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 19 Apr 2024
"""

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        def compute(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1': return
            grid[i][j] = '0'
            compute(i+1, j)
            compute(i-1, j)
            compute(i, j+1)
            compute(i, j-1)

        res, rows, cols = 0, len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                cell = grid[i][j]
                if cell == '1':
                    res += 1
                    compute(i, j)
        return res

# Time Complexity  : O(m * n)
# Space Complexity : O(m * n)