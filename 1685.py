"""
Title       : 1685. Sum of Absolute Differences in a Sorted Array
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 25 Nov 2023
Solved Using    : Python3
"""

from typing import List
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n, diff = len(nums), sum(nums)
        ans = [0] * n
        for i, num in enumerate(nums):
            ans[i] = (2 * i - n) * num + diff
            diff -= 2 * num
        return ans

# Time Complexity : O(n)
# Space Complexity : O(n)