"""
Title       : 1658. Minimum Operations to Reduce X to Zero
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 20 Sept 2023
Solved Using    : Python3
"""

from typing import List
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        target = total - x
        if x == total:
            return len(nums)
        if x > total:
            return -1
        l = cumSum = maxLen = 0
        for r in range(len(nums)):
            cumSum += nums[r]
            while l < r and cumSum > target:
                cumSum -= nums[l]
                l += 1
            if cumSum == target:
                maxLen = max(maxLen, r - l + 1)
        return len(nums) - maxLen if maxLen != 0 else -1

# Time Complexity  : O(n)
# Space Complexity : O(1)