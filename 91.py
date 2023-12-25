"""
Title       : 91. Decode Ways
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 25 Dec 2023
Solved Using    : Python3
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0': return 0
        prev, curr = 1, 1
        for i in range(2, len(s) + 1):
            temp = curr
            if s[i - 1] == '0':
                curr = 0
            if '10' <= s[i - 2:i] <= '26':
                curr += prev
            prev = temp
        return curr

# Time Complexity  : O(n)
# Space Complexity : O(1)