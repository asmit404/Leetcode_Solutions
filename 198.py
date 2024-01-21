"""
Title       : 198. House Robber
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 21 Jan 2024
"""

from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, var = nums[0], 0
        for i in range(1, len(nums)):
            prev, var = max(var + nums[i], prev), prev
        return prev

# Time Complexity: O(n)
# Space Complexity: O(1)