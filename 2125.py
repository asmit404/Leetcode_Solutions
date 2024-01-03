"""
Title       : 2125. Number of Laser Beams in a Bank
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 3 Jan 2024
"""

from typing import List
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = temp = 0
        for floor in bank:
            cnt = floor.count('1')
            if cnt == 0: continue
            res += temp * cnt
            temp = cnt
        return res

# Time Complexity  : O(n)
# Space Complexity : O(1)