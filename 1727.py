"""
Title       : 1727. Largest Submatrix With Rearrangements
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 26 Nov 2023
Solved Using    : Python3
"""

from typing import List
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n, res = len(matrix), len(matrix[0]), 0
        
        for j in range(n):
            for i in range(1, m):
                matrix[i][j] += matrix[i-1][j] if matrix[i][j] else 0
                
        for i in range(m): 
            matrix[i].sort()
            for j in range(n):
                res = max(res, (n-j)*matrix[i][j])
        return res

# Time Complexity : O(m*n*log(n))
# Space Complexity : O(1)