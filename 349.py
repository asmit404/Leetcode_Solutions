"""
Title       : 349. Intersection of Two Arrays
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 10 Mar 2024
"""

from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums2)-(set(nums2)-set(nums1)))

# Time Complexity  : O(n + m)
# Space Complexity : O(n + m)