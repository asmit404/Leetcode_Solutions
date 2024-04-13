"""
Title       : 85. Maximal Rectangle
Difficulty  : Hard
Author      : Asmit Singh
Solved On   : 13 Apr 2024
"""

from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]], res = 0) -> int:
        if not matrix or not matrix[0]: return 0
        n = len(matrix[0])
        height = [0] * (n + 1)

        for row in matrix:
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == '1' else 0

            pool = [-1]
            for i in range(n + 1):
                while height[i] < height[pool[-1]]:
                    h = height[pool.pop()]
                    w = i - pool[-1] - 1
                    res = max(res, h * w)
                pool.append(i)

        return res

# Time Complexity  : O(m * n)
# Space Complexity : O(n)