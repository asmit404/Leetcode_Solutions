"""
Title       : 1752. Check if Array Is Sorted and Rotated
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 2 Feb 2025
"""

from typing import List
class Solution:
    def check(self, nums: List[int]) -> bool:
        count, n = 0, len(nums)
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                count += 1
                if count > 1:
                    return False
                
        count += 1 if nums[-1] > nums[0] else 0
        return count <= 1

# Beats 100% of submissions in runtime
# Time Complexity: O(n)
# Space Complexity: O(1)