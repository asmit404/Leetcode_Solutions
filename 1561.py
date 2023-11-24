"""
Title       : 1561. Maximum Number of Coins You Can Get
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 24 Nov 2023
Solved Using    : Python3
"""

class Solution:
    def maxCoins(self, piles) -> int:
        return sum(sorted(piles)[len(piles) // 3::2])

# Time Complexity : O(nlog(n))
# Space Complexity : O(1)