"""
Title       : 896. Monotonic Array
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 29 Sept 2023
Solved Using    : Python3
"""

from typing import List
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        return all(nums[i] <= nums[i+1] for i in range(len(nums)-1)) or all(nums[i] >= nums[i+1] for i in range(len(nums)-1))

# Time Complexity  : O(n)
# Space Complexity : O(1)