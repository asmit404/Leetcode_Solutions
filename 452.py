"""
Title       : 452. Minimum Number of Arrows to Burst Balloons
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 18 Mar 2024
"""

from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[1])
        curr, cnt = float('-inf'), 0
        for p in points:
            if p[0] > curr:
                cnt += 1
                curr = p[1]
            else:
                continue
        return cnt

# Time Complexity  : O(n log n)
# Space Complexity : O(1)