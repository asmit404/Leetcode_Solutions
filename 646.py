"""
Title       : 646. Maximum Length of Pair Chain
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 26 Aug 2023
Solved Using    : Python3
"""

from typing import List
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        cur, res = float('-inf'), 0
        for pair in sorted(pairs, key=lambda x: x[1]):
            if cur < pair[0]:
                cur = pair[1]
                res += 1
        return res

# Time Complexity  : O(n log n)
# Space Complexity : O(1)