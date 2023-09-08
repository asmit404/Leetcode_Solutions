"""
Title       : 118. Pascal's Triangle
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 8 Sept 2023
Solved Using    : Python3
"""

from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = []
        for i in range(numRows):
            row = [1] * (i+1)
            for j in range(1, i):
                row[j] = rows[i-1][j-1] + rows[i-1][j]
            rows.append(row)
        return rows

# Time Complexity  : O(n ^ 2)
# Space Complexity : O(n ^ 2)