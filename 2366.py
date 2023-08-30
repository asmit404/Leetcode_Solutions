"""
Title       : 2366. Minimum Replacements to Sort the Array
Difficulty  : Hard
Author      : Asmit Singh
Solved On   : 30 Aug 2023
Solved Using    : Python3
"""

from typing import List
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        last = nums[n - 1]
        ops = 0

        for i in range(n - 2, -1, -1):
            if nums[i] > last:
                t = nums[i] // last
                if nums[i] % last:
                    t += 1
                last = nums[i] // t
                ops += t - 1
            else:
                last = nums[i]
        return ops

# Time Complexity  : O(n)
# Space Complexity : O(1)