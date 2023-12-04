"""
Title       : 2264. Largest 3-Same-Digit Number in String
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 04 Dec 2023
Solved Using    : Python3
"""

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        for i in range(0, len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                if num[i: i + 3] > res:
                    res = num[i: i + 3]
        return res

# Time Complexity : O(n)
# Space Complexity : O(1)