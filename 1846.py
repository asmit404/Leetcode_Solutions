"""
Title       : 1846. Maximum Element After Decreasing and Rearranging
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 15 Nov 2023
Solved Using    : Python3
"""

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        arr.sort()
        curr = 1
        for i in range(1, len(arr)):
            if arr[i] > curr:
                curr += 1
        return curr

# Time Complexity  : O(nlogn)
# Space Complexity : O(1)