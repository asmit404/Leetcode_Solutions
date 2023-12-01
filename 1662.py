"""
Title       : 1611. Check If Two String Arrays are Equivalent
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 01 Dec 2023
Solved Using    : Python3
"""

class Solution:
    def arrayStringsAreEqual(self, word1, word2) -> bool:
        return ''.join(word1) == ''.join(word2)

# Time Complexity : O(n)
# Space Complexity : O(n)