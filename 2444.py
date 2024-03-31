"""
Title       : 2444. Count Subarrays With Fixed Bounds
Difficulty  : Hard
Author      : Asmit Singh
Solved On   : 31 Mar 2024
"""

from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        min_idx = max_idx = bad_idx = -1
        for i, v in enumerate(nums):
            if v < minK or v > maxK:
                min_idx, max_idx, bad_idx = -1, -1, i
            if v == minK:
                min_idx = i
            if v == maxK:
                max_idx = i
            if min_idx > -1 and max_idx > -1:
                res += min(min_idx, max_idx) - bad_idx
        return res

# Time Complexity  : O(n)
# Space Complexity : O(1)