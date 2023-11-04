"""
Title       : 1503. Last Moment Before All Ants Fall Out of a Plank
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 04 Nov 2023
Solved Using    : Python3
"""

class Solution:
    def getLastMoment(self, n, left, right):
        return max(max(left, default=0), n - min(right, default=n))

# Beat 100% submissions in runtime
# Time Complexity  : O(n)
# Space Complexity : O(1)