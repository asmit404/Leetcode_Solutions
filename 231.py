"""
Title       : 231. Power of Two
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 19 Feb 2024
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1: return False
        return n & (n - 1) == 0

# Time Complexity: O(1)
# Space Complexity: O(1)