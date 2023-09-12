"""
Title       : 1647. Minimum Deletions to Make Character Frequencies Unique
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 12 Sept 2023
Solved Using    : Python3
"""

from collections import Counter
class Solution:
    def minDeletions(self, s: str) -> int:
        hashmap = Counter(s)
        freq = set()
        deletions = 0
        for char, count in hashmap.items():
            while count in freq and count > 0:
                deletions += 1
                count -= 1
            freq.add(count)
        return deletions

# Time Complexity  : O(n log n)
# Space Complexity : O(n)