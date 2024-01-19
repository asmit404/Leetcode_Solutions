"""
Title       : 931. Minimum Falling Path Sum
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 19 Jan 2024
"""

from typing import List
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0: return 0
        m, n, minSum = len(matrix), len(matrix[0]), float('inf')

        for i in range(1, m):
            for j in range(0, n):
                if j == 0:
                    matrix[i][j] = min(
                        matrix[i-1][j], matrix[i-1][j+1]) + matrix[i][j]
                elif j == n-1:
                    matrix[i][j] = min(
                        matrix[i-1][j], matrix[i-1][j-1]) + matrix[i][j]
                else:
                    matrix[i][j] = min(
                        matrix[i-1][j], matrix[i-1][j-1], matrix[i-1][j+1]) + matrix[i][j]

        for j in range(n):
            minSum = min(minSum, matrix[m-1][j])

        return minSum

# Time Complexity: O(m * n)
# Space Complexity: O(1)