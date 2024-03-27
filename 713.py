"""
Title       : 713. Subarray Product Less Than K
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 27 Mar 2024
"""

from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0
        left = res = 0
        curr = 1
        for right in range(len(nums)):
            curr *= nums[right]
            while curr >= k:
                curr //= nums[left]
                left += 1
            res += right - left + 1
        return res

# Time Complexity  : O(n)
# Space Complexity : O(1)