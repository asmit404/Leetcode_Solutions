"""
Title       : 1496. Path Crossing
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 23 Dec 2023
Solved Using    : Python3
"""

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = y = 0
        vis = set([(x, y)])
        dir_map = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
        for dir in path:
            dx, dy = dir_map[dir]
            x, y = x + dx, y + dy
            if (x, y) in vis:
                return True
            vis.add((x, y))
        return False

# Time Complexity  : O(n)
# Space Complexity : O(n)