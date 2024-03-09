"""
Title       : 2540. Minimum Common Value
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 09 Mar 2024
"""

from typing import List
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = 0
        l1, l2 = len(nums1), len(nums2)
        while i < l1 and j < l2:
            if nums1[i] == nums2[j]:
                return nums1[i]
            if nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return -1

# Time Complexity  : O(n + m)
# Space Complexity : O(1)