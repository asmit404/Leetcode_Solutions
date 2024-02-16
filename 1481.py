"""
Title       : 1481. Least Number of Unique Integers after K Removals
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 16 Feb 2024
"""

from typing import List
from collections import Counter
from heapq import heappop, heappush, heapify

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        heap = list(c.values())
        heapify(heap)
        while k > 0 and heap:
            min_val = heappop(heap)
            if k >= min_val:
                k -= min_val
            else:
                heappush(heap, min_val)
                break
        return len(heap)

# Time complexity: O(nlogn)
# Space complexity: O(n)