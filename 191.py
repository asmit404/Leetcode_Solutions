"""
Title       : 191. Number of 1 Bits
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 29 Nov 2023
Solved Using    : Python3
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

# Time Complexity : O(1)
# Space Complexity : O(1)