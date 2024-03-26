"""
Title       : 41. First Missing Positive
Difficulty  : Hard
Author      : Asmit Singh
Solved On   : 26 Mar 2024
"""

from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        pool, var = set(nums), 0
        for _ in nums:
            var += 1
            if var not in pool:
                return var
        return len(nums) + 1

# Time Complexity  : O(n)
# Space Complexity : O(n)