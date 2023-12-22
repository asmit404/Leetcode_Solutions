"""
Title       : 1422. Maximum Score After Splitting a String
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 22 Dec 2023
Solved Using    : Python3
"""

class Solution:
    def maxScore(self, s: str) -> int:
        score = s.count('1')
        return max((score := score + 1) if i == '0' else (score := score - 1) for i in s[:-1])

# Time Complexity  : O(n)
# Space Complexity : O(1)