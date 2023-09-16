"""
Title       : 1631. Path With Minimum Effort
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 16 Sept 2023
Solved Using    : Python3
"""

import heapq
from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights)-1, len(heights[0])-1
        d, heap = {(m, n): 0}, [(0, m, n)]
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        while heap:
            cur_effort, curx, cury = heapq.heappop(heap)
            if (curx, cury) == (0, 0):
                return cur_effort

            for dx, dy in dirs:
                nx, ny = curx + dx, cury + dy
                if 0 <= nx <= m and 0 <= ny <= n:
                    new_effort = max(cur_effort, abs(heights[curx][cury]-heights[nx][ny]))
                    if (nx, ny) not in d or new_effort < d[(nx, ny)]:
                        d[(nx, ny)] = new_effort
                        heapq.heappush(heap, (new_effort, nx, ny))

# Time Complexity  : O(mn log mn)
# Space Complexity : O(mn)