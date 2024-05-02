"""
Title       : 2441. Largest Positive Integer That Exists With Its Negative
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 2 May 2024
"""

from typing import List
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        return max((i for i in set(nums) if -i in nums), default=-1)

# Time Complexity  : O(n)
# Space Complexity : O(n)