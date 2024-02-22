"""
Title       : 1642. Furthest Building You Can Reach
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 17 Feb 2024
"""

from typing import List
from heapq import heappush, heappop

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff <= 0: continue
            bricks -= diff
            heappush(heap, -diff)
            if bricks < 0:
                if not ladders: return i
                ladders -= 1
                bricks += -heappop(heap)
        return len(heights) - 1

# Time Complexity: O(n log n)
# Space Complexity: O(n)