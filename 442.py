"""
Title       : 442. Find All Duplicates in an Array
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 25 Mar 2024
"""

from typing import List
from collections import Counter

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        return [num for num, count in Counter(nums).items() if count > 1]

# Time Complexity  : O(n)
# Space Complexity : O(n)