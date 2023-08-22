"""
Title       : 168. Excel Sheet Column Title
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 22 Aug 2023
Solved Using    : Python3
"""

class Solution(object):
    def convertToTitle(self, columnNumber):
        return "" if columnNumber == 0 else self.convertToTitle((columnNumber - 1) // 26) + chr((columnNumber - 1) % 26 + ord('A'))

# Time Complexity  : O(log n)
# Space Complexity : O(log n)