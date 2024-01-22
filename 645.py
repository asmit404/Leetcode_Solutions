"""
Title       : 645. Set Mismatch
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 22 Jan 2024
"""

from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        vis, dup, act_sum = set(), 0, 0
        exp_sum = n * (n + 1) // 2

        for num in nums:
            if num in vis:
                dup = num
            vis.add(num)
            act_sum += num

        miss = exp_sum - act_sum + dup
        return [dup, miss]

# Time Complexity  : O(n)
# Space Complexity : O(n)