"""
Title       : 739. Daily Temperatures
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 31 Jan 2024
"""

from collections import deque
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        pool = deque()
        for i, t in enumerate(temperatures):
            while pool and t > temperatures[pool[-1]]:
                idx = pool.pop()
                res[idx] = i - idx
            pool.append(i)
        return res

# Time Complexity  : O(n)
# Space Complexity : O(n)