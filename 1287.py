"""
Title       : 1287. Element Appearing More Than 25% In Sorted Array
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 11 Dec 2023
Solved Using    : Python3
"""

class Solution:
    def findSpecialInteger(self, arr) -> int:
        n = len(arr)
        qtr = n // 4
        for i in range(n - qtr):
            if arr[i] == arr[i + qtr]:
                return arr[i]

# Time Complexity  : O(n)
# Space Complexity : O(1)