"""
Title       : 1913. Maximum Product Difference Between Two Pairs
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 18 Dec 2023
Solved Using    : Python3
"""

from typing import List
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1] * nums[-2]) - (nums[0] * nums[1])

# Time Complexity  : O(nlogn)
# Space Complexity : O(1)