"""
Title       : 1758. Minimum Changes To Make Alternating Binary String
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 24 Dec 2023
Solved Using    : Python3
"""

class Solution:
    def minOperations(self, s: str) -> int:
        zero = one = 0 # Genius, I know
        for i in range(len(s)):
            if (i % 2 == 0 and s[i] == '0') or (i % 2 == 1 and s[i] == '1'):
                one += 1
            else:
                zero += 1
        return min(zero, one)

# Time Complexity  : O(n)
# Space Complexity : O(1)