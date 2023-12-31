"""
Title       : 1624. Largest Substring Between Two Equal Characters
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 31 Dec 2023
Solved Using    : Python3
"""

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        return max(s.rindex(ch) - s.index(ch) - 1 for ch in set(s))

# Closing 2023 with a 138 day streak.
# Time Complexity  : O(n ^ 2)
# Space Complexity : O(n)