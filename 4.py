"""
Title       : 4. Median of Two Sorted Arrays
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 20 Sept 2023
Solved Using    : Python3
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        pool = sorted(nums1 + nums2)
        total = len(pool)

        if total & 1 == 1:
            return float(pool[total // 2])
        else:
            mid1, mid2 = pool[total // 2 - 1], pool[total // 2]
            return (float(mid1) + float(mid2)) / 2.0

# There are better ways to solve this problem, but this is the simplest one.
# Time Complexity  : O((m+n)log(m+n))
# Space Complexity : O(m+n)