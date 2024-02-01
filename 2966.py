"""
Title       : 2966. Best Time to Buy and Sell Stock with Cooldown
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 01 Feb 2024
"""

from typing import List
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans, idx = [], 0
        while idx < len(nums):
            if nums[idx+2]-nums[idx] <= k:
                ans.append(nums[idx:idx+3])
            else:
                return []
            idx += 3
        return ans

# Time Complexity  : O(n log n)
# Space Complexity : O(n)