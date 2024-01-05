"""
Title       : 300. Longest Increasing Subsequence
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 5 Jan 2024
"""

from typing import List
from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        pool = []
        for num in nums:
            idx = bisect_left(pool, num)
            if idx == len(pool):
                pool.append(num)
            else:
                pool[idx] = num
        return len(pool)

# Time Complexity  : O(n log n)
# Space Complexity : O(n)