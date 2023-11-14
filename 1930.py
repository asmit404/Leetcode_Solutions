"""
Title       : 1930. Unique Length-3 Palindromic Subsequences
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 14 Nov 2023
Solved Using    : Python3
"""

from collections import defaultdict
from bisect import bisect_left

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        idx = defaultdict(list)
        for i, c in enumerate(s):
            idx[c].append(i)
        cnt = 0
        for c, i in idx.items():
            if len(i) > 2:
                cnt += 1
            for k, j in idx.items():
                if c == k:
                    continue
                bisect_left_result = bisect_left(j, i[0])
                if bisect_left_result < bisect_left(j, i[-1]):
                    cnt += 1
        return cnt

# Beats 100% of submissions in runtime
# Time Complexity  : O(n)
# Space Complexity : O(n)