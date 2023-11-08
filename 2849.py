"""
Title       : 2849. Determine if a Cell Is Reachable at a Given Time
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 08 Nov 2023
Solved Using    : Python3
"""

class Solution:
    def isReachableAtTime(self, sx, sy, fx, fy, t):
        first = abs(sx-fx)
        second = abs(sy-fy)
        total = max(first, second)
        if total > t or (total == 0 and t == 1):
            return False
        return True

# Time Complexity  : O(1)
# Space Complexity : O(1)