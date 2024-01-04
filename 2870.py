"""
Title       : 2870. Minimum Number of Operations to Make Array Empty
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 4 Jan 2024
"""

from math import ceil
from typing import List
from collections import Counter

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt, res = Counter(nums), 0
        for count in cnt.values():
            if count == 1: return -1
            res += ceil(count / 3)
        return res

# Time Complexity  : O(n)
# Space Complexity : O(n)