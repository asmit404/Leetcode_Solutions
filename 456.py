"""
Title       : 456. 132 Pattern
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 30 Sept 2023
Solved Using    : Python3
"""

from typing import List
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        pool = []
        num = float('-inf')
        for n in reversed(nums):
            if n < num:
                return True
            while pool and pool[-1] < n:
                num = pool.pop()
            pool.append(n)
        return False

# Time Complexity  : O(n)
# Space Complexity : O(n)