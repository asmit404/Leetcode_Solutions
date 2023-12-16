"""
Title       : 242. Valid Anagram
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 16 Dec 2023
Solved Using    : Python3
"""

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

# Time Complexity  : O(n)
# Space Complexity : O(n)