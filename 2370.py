"""
Title       : 2370. Longest Common Subsequence
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 25 Apr 2024
"""

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        pool = [0] * 128
        for char in s:
            i = ord(char)
            pool[i] = max(pool[i - k: i + k + 1]) + 1
        return max(pool)

# Time Complexity  : O(n * k)
# Space Complexity : O(1)