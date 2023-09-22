"""
Title       : 392. Is Subsequence
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 22 Sept 2023
Solved Using    : Python3
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index = 0
        for char in t:
            if s_index == len(s):
                return True
            if char == s[s_index]:
                s_index += 1
        return s_index == len(s)

# Time Complexity  : O(n)
# Space Complexity : O(1)