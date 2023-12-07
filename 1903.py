"""
Title       : 1903. Largest Odd Number in String
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 07 Dec 2023
Solved Using    : Python3
"""

class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if num[i] in "13579":
                return num[:i + 1]
        return ""

# Time Complexity : O(n)
# Space Complexity : O(1)