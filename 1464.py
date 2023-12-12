"""
Title       : 1464. Maximum Product Of Two Elements In An Array
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 12 Dec 2023
Solved Using    : Python3
"""

import heapq
class Solution:
    def maxProduct(self, nums) -> int:
        max1, max2 = heapq.nlargest(2, nums)
        return (max1 - 1) * (max2 - 1)

# Time Complexity  : O(n log n)
# Space Complexity : O(n)