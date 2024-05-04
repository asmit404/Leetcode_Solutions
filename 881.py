"""
Title       : 881. Boats to Save People
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 4 May 2024
"""

from typing import List
class Solution:
    def numRescueBoats(self, p: List[int], limit: int) -> int:
        p.sort()
        left, right = 0, len(p) - 1
        boats = 0
        while left <= right:
            if p[left] + p[right] <= limit:
                left += 1
            right -= 1
            boats += 1
        return boats

# Time Complexity  : O(n log n)
# Space Complexity : O(1)