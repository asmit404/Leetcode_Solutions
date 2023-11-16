"""
Title       : 1980. Find Unique Binary String
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 16 Nov 2023
Solved Using    : Python3
"""

class Solution:
    def findDifferentBinaryString(self, nums) -> str:
        return "".join('0' if nums[i][i] == '1' else '1' for i in range(len(nums)))

# Time Complexity  : O(n)
# Space Complexity : O(n)