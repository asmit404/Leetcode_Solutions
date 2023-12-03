"""
Title       : 1266. Minimum Time Visiting All Points
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 03 Dec 2023
Solved Using    : Python3
"""

from typing import List
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        for i in range(1, len(points)):
            dx = abs(points[i][0] - points[i-1][0])
            dy = abs(points[i][1] - points[i-1][1])
            time += max(dx, dy)
        return time

# Time Complexity : O(n)
# Space Complexity : O(1)