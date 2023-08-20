"""
Title       : 542. 01 Matrix
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 17 Aug 2023
Solved Using    : Python3
"""

from typing import List
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        for i in range(n):
            for j in range(m):
                if mat[i][j] != 0:
                    top = mat[i-1][j] if i > 0 else float('inf')
                    left = mat[i][j-1] if j > 0 else float('inf')
                    mat[i][j] = min(top, left) + 1
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if mat[i][j] != 0:
                    bottom = mat[i+1][j] if i < n-1 else float('inf')
                    right = mat[i][j+1] if j < m-1 else float('inf')
                    mat[i][j] = min(mat[i][j], bottom+1, right+1)
        return mat

# Time Complexity : O(n*m)
# Space Complexity : O(1)