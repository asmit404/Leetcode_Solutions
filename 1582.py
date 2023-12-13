"""
Title       : 1582. Special Positions In A Binary Matrix
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 13 Dec 2023
Solved Using    : Python3
"""

from typing import List
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        v = [i for i, r in enumerate(mat) if sum(r) == 1]
        h = [i for i, c in enumerate(zip(*mat)) if sum(c) == 1]
        return sum(mat[r][c] for r in v for c in h)

# Time Complexity  : O(n^2)
# Space Complexity : O(n)