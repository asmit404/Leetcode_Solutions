"""
Title       : 238. Product of Array Except Self
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 15 Mar 2024
"""

from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lp = [0] * n
        rp = [0] * n
        res = [0] * n

        lp[0] = 1
        for i in range(1, n):
            lp[i] = nums[i - 1] * lp[i - 1]

        rp[n - 1] = 1
        for i in reversed(range(n - 1)):
            rp[i] = nums[i + 1] * rp[i + 1]

        for i in range(n):
            res[i] = lp[i] * rp[i]

        return res

# Time Complexity  : O(n)
# Space Complexity : O(n)