"""
Title       : 2971. Find Polygon With the Largest Perimeter
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 15 Feb 2024
"""

from typing import List
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        pool = sorted(nums)
        _sum = sum(nums)
        while len(pool) > 2:
            if pool[-1] < _sum - pool[-1]: return _sum
            _sum -= pool.pop()
        return -1

# Time complexity: O(nlogn)
# Space complexity: O(1)