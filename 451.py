"""
Title       : 451. Sort Characters By Frequency
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 07 Feb 2024
"""

from collections import Counter
from heapq import heapify, heappop

class Solution:
    def frequencySort(self, s: str) -> str:
        cnt, res = Counter(s), []
        pq = [(-freq, char) for char, freq in cnt.items()]
        heapify(pq)
        while pq:
            freq, char = heappop(pq)
            res.extend([char] * -freq)
        return ''.join(res)

# Time complexity: O(nlogn)
# Space complexity: O(n)