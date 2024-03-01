"""
Title       : 2864. Maximum Odd Binary Number
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 01 Mar 2024
"""

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count('1')
        return ('1' * (ones - 1)) + ('0' * (len(s) - ones)) + '1'

# Time Complexity: O(n)
# Space Complexity: O(n)