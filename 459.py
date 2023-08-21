"""
Title       : 459. Repeated Substring Pattern
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 21 Aug 2023
Solved Using    : Python3
"""

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        s1 = s+s
        s1 = s1[1:-1]
        return (s in s1)

# Time Complexity  : O(n)
# Space Complexity : O(n)