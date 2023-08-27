"""
Title       : 403. Frog Jump
Difficulty  : Hard
Author      : Asmit Singh
Solved On   : 27 Aug 2023
Solved Using    : Python3
"""

from typing import List
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        ss = set(stones)
        vis = set()
        pool = [(0, 0)]
        while pool:
            stone, jump = pool.pop()
            for j in [jump-1, jump, jump+1]:
                s = stone + j
                if j > 0 and s in ss and (s, j) not in vis:
                    if s == stones[-1]:
                        return True
                    pool.append((s, j))
            vis.add((stone, jump))
        return False

# Time Complexity  : O(n^2)
# Space Complexity : O(n^2)