"""
Title       : 169. Majority Element
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 12 Feb 2024
"""

from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) < 2: return nums[0]
        nums.sort()
        pos = (len(nums) - 1) // 2
        return nums[pos]

# Time complexity: O(n log n)
# Space complexity: O(1)