"""
Title       : 76. Minimum Window Substring
Difficulty  : Hard
Author      : Asmit Singh
Solved On   : 04 Feb 2024
"""

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t): return ""
        count, missing = Counter(t), len(t)
        l, start, min_len = 0, 0, float('inf')

        for r, char in enumerate(s, 1):
            if count[char] > 0:
                missing -= 1
            count[char] -= 1

            if missing == 0:
                while count[s[l]] < 0:
                    count[s[l]] += 1
                    l += 1
                if r - l < min_len:
                    min_len = r - l
                    start = l

        return "" if min_len == float('inf') else s[start : start + min_len]

# Time Complexity  : O(n)
# Space Complexity : O(m)