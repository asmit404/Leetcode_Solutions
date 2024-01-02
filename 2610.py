"""
Title       : 2610. Convert an Array Into a 2D Array With Conditions
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 2 Jan 2024
"""

from typing import List
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []
        for num in nums:
            for group in res:
                if num not in group:
                    group.add(num)
                    break
            else:
                res.append({num})
        return res

# Time Complexity  : O(n^2)
# Space Complexity : O(n)