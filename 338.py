"""
Title       : 338. Counting Bits
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 1 Sept 2023
Solved Using    : Python3
"""

from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(1, n + 1):
            res[i] = res[i >> 1] + (i & 1)
        return res

# Time Complexity  : O(n)
# Space Complexity : O(n)