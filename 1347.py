"""
Title       : 1347. Minimum Number of Steps to Make Two Strings Anagram
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 13 Jan 2024
"""

from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt_s = Counter(s)
        cnt_t = Counter(t)
        return sum((cnt_t - cnt_s).values())

# Time complexity: O(n)
# Space complexity: O(n)