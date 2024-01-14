"""
Title       : 1657. Determine if Two Strings Are Close
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 14 Jan 2024
"""

from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return set(word1) == set(word2) and Counter(Counter(word1).values()) == Counter(Counter(word2).values())

# Time complexity: O(n)
# Space complexity: O(n)