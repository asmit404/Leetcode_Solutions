"""
Title       : 201. Bitwise AND of Numbers Range
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 21 Feb 2024
"""

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left < right:
            right = right & (right-1)
        return left & right

# Time Complexity: O(log n)
# Space Complexity: O(1)