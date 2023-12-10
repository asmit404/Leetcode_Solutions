"""
Title       : 867. Transpose Matrix
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 10 Dec 2023
Solved Using    : Python3
"""

class Solution:
    def transpose(self, matrix):
        return zip(*matrix)

# Time Complexity  : O(n)
# Space Complexity : O(n)