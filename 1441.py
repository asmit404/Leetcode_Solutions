"""
Title       : 1441. Build an Array With Stack Operations
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 03 Nov 2023
Solved Using    : Python3
"""

class Solution:
    def buildArray(self, target, n):
        res = []
        t_set = set(target)
        for i in range(1, target[-1] + 1):
            res.append("Push")
            if i not in t_set:
                res.append("Pop")
        return res

# Time Complexity  : O(n)
# Space Complexity : O(n)