"""
Title       : 389. Find the Difference
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 25 Sept 2023
Solved Using    : Python3
"""

from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return (Counter(t) - Counter(s)).popitem()[0]

# Time Complexity  : O(n)
# Space Complexity : O(1)