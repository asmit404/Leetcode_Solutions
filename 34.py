"""
Title       : 34. Find First and Last Position of Element in Sorted Array
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 9 Oct 2023
Solved Using    : Python3
"""

from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        pool = []
        for i in range(len(nums)):
            if nums[i] == target:
                pool.append(i)
        if not pool:
            return [-1, -1]
        else:
            return [pool[0], pool[-1]]

# Could be done using binary search in O(log n), but I'm too lazy to do that
# Time Complexity  : O(n)
# Space Complexity : O(n)