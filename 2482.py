"""
Title       : 2482. Difference Between Ones and Zeros in Row and Column
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 14 Dec 2023
Solved Using    : Python3
"""

from typing import List
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        RowOne = [row.count(1) for row in grid]
        ColOne = [col.count(1) for col in zip(*grid)]
        RowZero = [m - one for one in RowOne]
        ColZero = [n - one for one in ColOne]
        res = [[RowOne[i] + ColOne[j] - RowZero[i] - ColZero[j] for j in range(n)] for i in range(m)]
        return res

# Time Complexity  : O(mn)
# Space Complexity : O(mn)