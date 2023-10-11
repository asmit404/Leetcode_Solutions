"""
Title       : 2009. Minimum Number of Operations to Make Array Continuous
Difficulty  : Hard
Author      : Asmit Singh
Solved On   : 10 Oct 2023
Solved Using    : Python3
"""

from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nLen = len(nums)
        nums = sorted(set(nums))
        res = lp = 0
        for rp, num in enumerate(nums):
            if num - nums[lp] >= nLen:
                lp += 1
            res = max(res, rp - lp + 1)
        return nLen - res

# Time Complexity  : O(n log n)
# Space Complexity : O(n)