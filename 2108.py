"""
Title       : 2108. Find First Palindromic String in the Array
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 13 Feb 2024
"""

from typing import List
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        return next((s for s in words if s == s[::-1]), "")

# Time complexity: O(n * m)
# Space complexity: O(m)