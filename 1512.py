"""
Title       : 1512. Number of Good Pairs
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 3 Oct 2023
Solved Using    : Python3
"""

from typing import List
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt = 0
        for i, num in enumerate(nums):
            cnt += nums[i+1:].count(num)
        return cnt

# Time Complexity  : O(n^2)
# Space Complexity : O(1)