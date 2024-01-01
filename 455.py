"""
Title       : 455. Assign Cookies
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 1 Jan 2024
"""

import heapq
from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        heapq.heapify(g)
        heapq.heapify(s)
        child = cookie = 0
        while g and s:
            if s[0] >= g[0]:
                heapq.heappop(g)
                child += 1
            heapq.heappop(s)
            cookie += 1
        return child

# Time Complexity  : O(n log n)
# Space Complexity : O(n)