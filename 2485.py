"""
Title       : 2485. Find the Pivot Integer
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 13 Mar 2024
"""

from math import sqrt
class Solution(object):
    def pivotInteger(self, n):
        return -1 if sqrt(n * (n + 1) / 2) % 1 != 0 else int(sqrt(n * (n + 1) / 2))

# Time Complexity  : O(1)
# Space Complexity : O(1)