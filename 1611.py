"""
Title       : 1611. Minimum One Bit Operations to Make Integers Zero
Difficulty  : Hard
Author      : Asmit Singh
Solved On   : 30 Nov 2023
Solved Using    : Python3
"""

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        res = 0
        while n:
            res ^= n
            n >>= 1
        return res

# Time Complexity : O(log n)
# Space Complexity : O(1)