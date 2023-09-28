"""
Title       : 905. Sort Array By Parity
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 28 Sept 2023
Solved Using    : Python3
"""

class Solution:
    def sortArrayByParity(self, nums):
        return sorted(nums, key=lambda x: x % 2)

# Time Complexity  : O(nlogn)
# Space Complexity  : O(n)