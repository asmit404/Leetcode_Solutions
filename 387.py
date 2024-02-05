"""
Title       : 387. First Unique Character in a String
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 05 Feb 2024
"""

from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        return next((i for i, char in enumerate(s) if counter[char] == 1), -1)

# Time Complexity  : O(n)
# Space Complexity : O(n)