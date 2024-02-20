"""
Title       : 268. Missing Number
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 20 Feb 2024
"""

from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return list(set(range(len(nums) + 1)) - set(nums))[0]

# Time Complexity: O(n)
# Space Complexity: O(n)