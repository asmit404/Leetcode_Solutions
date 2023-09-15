"""
Title       : 1584. Min Cost to Connect All Points
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 15 Sept 2023
Solved Using    : Python3
"""

from typing import List
class Solution:
    def get_distance(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        min_dist_map = {tuple(p): 0 if i == 0 else float('inf') for i, p in enumerate(points)}
        total_min_d = 0
        while min_dist_map:
            min_p = min(min_dist_map, key=min_dist_map.get)
            total_min_d += min_dist_map.pop(min_p)
            for k in min_dist_map:
                new_d = self.get_distance(min_p, k)
                if new_d < min_dist_map[k]:
                    min_dist_map[k] = new_d
        return total_min_d

# Time Complexity  : O(n^2 log n)
# Space Complexity : O(n)