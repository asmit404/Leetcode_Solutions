"""
Title       : 1249. Minimum Remove to Make Valid Parentheses
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 6 Apr 2024
"""

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s = list(s)
        for index, item in enumerate(s):
            if item == '(':
                stack.append(index)
            elif item == ')':
                if stack:
                    stack.pop()
                else:
                    s[index] = ''
        for item in stack:
            s[item] = ''
        return "".join(s)

# Time Complexity  : O(n)
# Space Complexity : O(n)