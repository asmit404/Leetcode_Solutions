"""
Title       : 2391. Minimum Amount of Time to Collect Garbage
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 20 Nov 2023
Solved Using    : Python3
"""

from typing import List

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        ans = 0
        n = len(garbage)
        m = p = g = False
        for i in range(n - 1, -1, -1):
            if not g and "G" in garbage[i]:
                g = True
                ans += sum(travel[:i])
            if not m and "M" in garbage[i]:
                m = True
                ans += sum(travel[:i])
            if not p and "P" in garbage[i]:
                p = True
                ans += sum(travel[:i])
            if all([m, p, g]):
                break

        return len("".join(garbage)) + ans

# Time Complexity : O(n^2)?
# Space Complexity : O(n)?