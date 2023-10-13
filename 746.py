"""
Title       : 746. Min Cost Climbing Stairs
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 13 Oct 2023
Solved Using    : Python3
"""

from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev1, prev2 = cost[1], cost[0]
        for i in range(2, len(cost)):
            prev1, prev2 = min(prev1, prev2) + cost[i], prev1
        return min(prev1, prev2)

# Time Complexity  : O(n)
# Space Complexity : O(1)