"""
Title       : 1239. Maximum Length of a Concatenated String with Unique Characters
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 23 Jan 2024
"""

from typing import List
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = [set()]
        for s in arr:
            if len(set(s)) != len(s): continue
            s = set(s)
            dp = dp + [d | s for d in dp if not d & s]
        return max(len(a) for a in dp)

# Time Complexity  : O(n * 2^n)
# Space Complexity : O(n * 2^n)