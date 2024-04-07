"""
Title       : 678. Valid Parenthesis String
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 7 Apr 2024
"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        lower = upper = 0
        for c in s:
            lower += 1 if c == '(' else -1
            upper -= 1 if c == ')' else -1
            if upper < 0: break
            lower = max(lower, 0)
        return lower == 0

# Time Complexity  : O(n)
# Space Complexity : O(1)