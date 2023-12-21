"""
Title       : 1637. Widest Vertical Area Between Two Points Containing No Points
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 21 Dec 2023
Solved Using    : Python3
"""

from typing import List
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        return max(points[i][0] - points[i-1][0] for i in range(1, len(points)))

# Time Complexity  : O(n log n)
# Space Complexity : O(1)