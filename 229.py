"""
Title       : 229. Majority Element II
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 5 Oct 2023
Solved Using    : Python3
"""

from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        l = len(nums)//3
        pool = [i for i in set(nums) if nums.count(i) > l]
        return pool

# Time Complexity  : O(n)
# Space Complexity : O(n)