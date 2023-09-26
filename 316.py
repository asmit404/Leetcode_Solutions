"""
Title       : 316. Remove Duplicate Letters
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 26 Sept 2023
Solved Using    : Python3
"""

from collections import defaultdict

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        char_count = defaultdict(int)
        for char in s:
            char_count[char] += 1
        pool = []
        vis = set()
        for char in s:
            char_count[char] -= 1
            if char in vis:
                continue
            while pool and char_count[pool[-1]] >= 1 and pool[-1] > char:
                vis.remove(pool.pop())
            vis.add(char)
            pool.append(char)
        return "".join(pool)

# Time Complexity  : O(n)
# Space Complexity : O(1)