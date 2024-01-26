"""
Title       : 576. Out of Boundary Paths
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 26 Jan 2024
"""

from functools import cache
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @cache
        def compute(i, j, moves):
            if i >= m or j >= n or i < 0 or j < 0: return 1
            elif moves == 0: return 0
            res = compute(i+1, j, moves-1)
            res += compute(i-1, j, moves-1)
            res += compute(i, j+1, moves-1)
            res += compute(i, j-1, moves-1)
            return res
        return compute(startRow, startColumn, maxMove) % (10**9+7)

# Time Complexity  : O(m * n * maxMove)
# Space Complexity : O(m * n * maxMove)