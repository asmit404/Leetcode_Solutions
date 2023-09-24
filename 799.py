"""
Title       : 799. Champagne Tower
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 24 Sept 2023
Solved Using    : Python3
"""

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [0] * (query_row + 2)
        tower[0] = poured

        for row in range(1, query_row + 1):
            for glass in range(row, -1, -1):
                tower[glass] = max(0, (tower[glass] - 1) / 2.0)
                tower[glass + 1] += tower[glass]

        return min(1.0, tower[query_glass])

# Time Complexity  : O(n^2)
# Space Complexity : O(n)