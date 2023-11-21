"""
Title       : 1814. Count Nice Pairs in an Array
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 21 Nov 2023
Solved Using    : Python3
"""

from typing import List
from collections import Counter

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        mod = 1000000007
        freq = Counter(num - int(str(num)[::-1]) for num in nums)
        res = 0
        for v in freq.values():
            res += v*(v-1)//2
        return res % mod

# Time Complexity : O(n)
# Space Complexity : O(n)