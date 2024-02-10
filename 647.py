"""
Title       : 647. Palindromic Substrings
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 10 Feb 2024
"""

class Solution:
    def countSubstrings(self, S: str) -> int:
        res, n, curr = 0, len(S), 0
        while (curr < n):
            lidx, ridx = curr - 1, curr
            while ridx < n - 1 and S[ridx] == S[ridx+1]:
                ridx += 1
            res += (ridx - lidx) * (ridx - lidx + 1) // 2
            curr, ridx = ridx + 1, ridx + 1
            while ~lidx and ridx < n and S[ridx] == S[lidx]:
                lidx, ridx, res = lidx - 1, ridx + 1, res + 1
        return res

# Time complexity: O(n ^ 2)
# Space complexity: O(1)