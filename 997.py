"""
Title       : 997. Find the Town Judge
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 22 Feb 2024
"""

from typing import List
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1: return 1 if not trust else -1
        diff = [0] * (n+1)
        for u, v in trust:
            diff[u] -= 1
            diff[v] += 1
        return next((u for u, d in enumerate(diff) if d == n - 1), -1)

# Time Complexity: O(n)
# Space Complexity: O(n)