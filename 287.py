"""
Title       : 287. Find the Duplicate Number
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 19 Sept 2023
Solved Using    : Python3
"""

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        vis = set()
        for num in nums:
            if num in vis:
                return num
            vis.add(num)

# Time Complexity  : O(n)
# Space Complexity : O(n)