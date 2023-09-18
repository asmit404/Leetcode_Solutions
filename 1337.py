"""
Title       : 1337. The K Weakest Rows in a Matrix
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 18 Sept 2023
Solved Using    : Python3
"""

from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        arr = [(sum(mat[r]), r) for r in range(len(mat))]
        return [row for _, row in sorted(arr)[:k]]

# Time Complexity  : O(m * n * log k)
# Space Complexity : O(m)