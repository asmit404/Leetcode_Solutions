"""
Title       : 343. Integer Break
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 6 Oct 2023
Solved Using    : Python3
"""

class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 4:
            return n - 1
        res = 1
        while n > 4:
            res *= 3
            n -= 3
        return res * n

# Don't ask me why this works, I don't know either.
# Time Complexity  : O(log n)
# Space Complexity : O(1)