"""
Title       : 119. Pascal's Triangle II
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 16 Oct 2023
Solved Using    : Python3
"""

from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(1, rowIndex+1):
            row.append(row[-1] * (rowIndex-i+1) // i)
        return row

# Beat 100% submissions in runtime.
# Time Complexity  : O(n)
# Space Complexity : O(n)