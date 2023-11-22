"""
Title       : 1424. Diagonal Traverse II
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 22 Nov 2023
Solved Using    : Python3
"""

from typing import List
from collections import deque

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        pool = []
        dq = deque()
        dq.append([0, 0])
        n = len(nums)
        while dq:
            i, j = dq.popleft()
            pool.append(nums[i][j])
            if j == 0 and i + 1 < n:
                dq.append([i + 1, j])
            if j + 1 < len(nums[i]):
                dq.append([i, j + 1])
        return pool

# Time Complexity : O(n)
# Space Complexity : O(n)