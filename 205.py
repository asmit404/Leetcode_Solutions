"""
Title       : 205. Isomorphic Strings
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 2 Apr 2024
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))

# Time Complexity  : O(n)
# Space Complexity : O(n)