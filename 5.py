"""
Title       : 5. Longest Palindromic Substring
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 27 Oct 2023
Solved Using    : Python3
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]: return s
        start, size = 0, 1
        for i in range(1, len(s)):
            l, r = i - size, i + 1
            if l - 1 >= 0 and s[l-1:r] == s[l-1:r][::-1]:
                start, size = l - 1, size + 2
            elif s[l:r] == s[l:r][::-1]:
                start, size = l, size + 1
        return s[start:start+size]

# Beat 100% submissions in runtime.
# Time Complexity  : O(n^2)
# Space Complexity : O(1)