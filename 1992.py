"""
Title       : 1992. Find All Groups of Farmland
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 20 Apr 2024
"""

from typing import List
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        res = []
        m, n = len(land), len(land[0])
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1 and (i == 0 or land[i-1][j] == 0) and (j == 0 or land[i][j-1] == 0):
                    x, y = i, j
                    while y+1 < n and land[x][y+1] == 1:
                        y += 1
                    while x+1 < m and land[x+1][y] == 1:
                        x += 1
                    res.append([i, j, x, y])
        return res

# Time Complexity  : O(m * n)
# Space Complexity : O(k)