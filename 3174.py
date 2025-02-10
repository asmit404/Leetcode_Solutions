"""
Title       : 3174. Clear Digits
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 10 Feb 2025
"""

class Solution:
    def clearDigits(self, s: str) -> str:
        pool = []
        for char in s:
            if char.isalpha():
                pool.append(char)
            else:
                pool.pop()
        return ''.join(pool)

# Beats 100% of submissions in runtime
# Time Complexity: O(n)
# Space Complexity: O(n)