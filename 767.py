"""
Title       : 767. Reorganize String
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 23 Aug 2023
Solved Using    : Python3
"""

class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = [(s.count(c), c) for c in set(s)]
        freq.sort(reverse=True)

        if freq[0][0] > (len(s) + 1) // 2:
            return ""

        res = [None] * len(s)
        i = 0
        for f, c in freq:
            for _ in range(f):
                if i >= len(s):
                    i = 1
                res[i] = c
                i += 2

        return "".join(res)

# Time Complexity  : O(n log n)
# Space Complexity : O(1)