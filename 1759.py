"""
Title       : 1759. Count Number of Homogenous Substrings
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 09 Nov 2023
Solved Using    : Python3
"""

class Solution:
    def countHomogenous(self, s: str) -> int:
        res, cnt = 0, 1
        MOD = 1000000007
        temp = s[0]
        for i in s[1:]:
            if i != temp:
                res += cnt*(cnt+1)//2
                cnt = 1
                temp = i
            else:
                cnt += 1
        res += cnt*(cnt+1)//2
        return res % MOD

# Time Complexity  : O(n)
# Space Complexity : O(1)