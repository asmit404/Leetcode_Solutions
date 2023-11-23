"""
Title       : 1630. Arithmetic Subarrays
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 23 Nov 2023
Solved Using    : Python3
"""

from typing import List

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        pool = []
        for a, b in zip(l, r):
            lst = sorted(nums[a:b+1])
            if len(lst) > 2:
                diff = lst[1] - lst[0]
                is_arithmetic = True
                for i in range(2, len(lst)):
                    if lst[i] - lst[i-1] != diff:
                        is_arithmetic = False
                        break
            else:
                is_arithmetic = True
            pool.append(is_arithmetic)
        return pool

# Time Complexity : O(mnlog(n))?
# Space Complexity : O(n)