"""
Title       : 1614. Maximum Nesting Depth of the Parentheses
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 4 Apr 2024
"""

class Solution:
    def maxDepth(self, s):
        cnt = maxN = 0
        for i in s:
            if i == "(":
                cnt += 1
                if maxN < cnt:
                    maxN = cnt
            if i == ")":
                cnt -= 1
        return maxN

# Time Complexity  : O(n)
# Space Complexity : O(1)