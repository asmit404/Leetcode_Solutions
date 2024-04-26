"""
Title       : 1289. Minimum Falling Path Sum II
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 26 Apr 2024
"""

from typing import List
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        pool = grid[0]
        for i in range(1, n):
            idx1, idx2 = sorted([(val, idx) for idx, val in enumerate(pool)])[:2]
            for j in range(n):
                if j != idx1[1]:
                    grid[i][j] += idx1[0]
                else:
                    grid[i][j] += idx2[0]
            pool = grid[i]
        return min(pool)

# Time Complexity  : O(n ^ 2)
# Space Complexity : O(n)