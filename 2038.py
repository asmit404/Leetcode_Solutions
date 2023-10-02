"""
Title       : 2038. Remove Colored Pieces if Both Neighbors are the Same Color
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 2 Oct 2023
Solved Using    : Python3
"""

import re
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a = sum(len(match.group()) - 2 for match in re.finditer(r'A{3,}', colors))
        b = sum(len(match.group()) - 2 for match in re.finditer(r'B{3,}', colors))
        return a > b

# Time Complexity  : O(n)
# Space Complexity : O(n)