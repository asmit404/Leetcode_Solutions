"""
Title       : 2147. Number of Ways to Divide a Long Corridor
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 28 Nov 2023
Solved Using    : Python3
"""

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 1000000007
        l, m, r = 0, 0, 1
        for i in corridor:
            if i == "S":
                l = m
                m, r = r, m
            else:
                r = (r + l) % MOD
        return l

# Time Complexity : O(n)
# Space Complexity : O(1)