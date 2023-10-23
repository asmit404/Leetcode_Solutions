"""
Title       : 342. Power of Four
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 23 Oct 2023
Solved Using    : Python3
"""

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n > 1:
            if n % 4 != 0:
                return False
            n //= 4
        return n == 1 if n > 0 else False

# Time Complexity  : O(log n)
# Space Complexity : O(1)