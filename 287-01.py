"""
Title       : 287. Find the Duplicate Number
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 24 Mar 2024
"""

from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        vis = set()
        return next(num for num in nums if num in vis or vis.add(num))

# Time Complexity  : O(n)
# Space Complexity : O(n)