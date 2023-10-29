"""
Title       : 458. Poor Pigs
Difficulty  : Hard
Author      : Asmit Singh
Solved On   : 29 Oct 2023
Solved Using    : Python3
"""

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        pigs = 0
        while (minutesToTest // minutesToDie + 1) ** pigs < buckets:
            pigs += 1
        return pigs

# Time Complexity  : O(log(n))
# Space Complexity : O(1)