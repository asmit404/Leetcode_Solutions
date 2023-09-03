"""
Title       : 62. Unique Paths
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 3 Sept 2023
Solved Using    : Python3
"""

import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m + n - 2, m - 1)

# Time Complexity  : O(1)
# Space Complexity : O(1)