"""
Title       : 779. K-th Symbol in Grammar
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 25 Oct 2023
Solved Using    : Python3
"""

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        k -= 1 # 0-indexed
        res = 0
        while k:
            res ^= k & 1
            k >>= 1
        return res

# Time Complexity  : O(log k)
# Space Complexity : O(1)