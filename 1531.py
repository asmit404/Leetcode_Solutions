"""
Title       : 1531. String Compression II
Difficulty  : Hard
Author      : Asmit Singh
Solved On   : 28 Dec 2023
Solved Using    : Python3
"""

from functools import cache
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        @cache
        def counter(start, last, cnt, left):
            if left < 0: return float('inf')
            if start >= n: return 0
            if s[start] == last:
                incr = 0
                if cnt in {1, 9, 99}:
                    incr = 1
                return incr + counter(start+1, last, cnt+1, left)
            else:
                keep = 1 + counter(start+1, s[start], 1, left)
                rem = counter(start + 1, last, cnt, left - 1)
                return min(keep, rem)
        return counter(0, "", 0, k)

# Time Complexity  : O(n ^ 2 * k)
# Space Complexity : O(n * k)