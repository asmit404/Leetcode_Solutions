"""
Title       : 2251. Number of Flowers in Full Bloom
Difficulty  : Hard
Author      : Asmit Singh
Solved On   : 11 Oct 2023
Solved Using    : Python3
"""

from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        start = sorted(s for s, _ in flowers)
        end = sorted(e for _, e in flowers)
        return [bisect_right(start, t) - bisect_left(end, t) for t in people]

# Beat 100% submissions in runtime.
# Time Complexity  : O(n log n)
# Space Complexity : O(n)