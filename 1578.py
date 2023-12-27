"""
Title       : 1578. Minimum Time to Make Rope Colorful
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 27 Dec 2023
Solved Using    : Python3
"""

from typing import List
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = idx = 0
        for i in range(1, len(colors)):
            if colors[i] == colors[idx]:
                res += min(neededTime[i], neededTime[idx])
                if neededTime[i] >= neededTime[idx]:
                    idx = i
            else:
                idx = i
        return res

# Time Complexity  : O(n)
# Space Complexity : O(1)