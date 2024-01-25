"""
Title       : 1143. Longest Common Subsequence
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 25 Jan 2024
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = map(len, (text1, text2))
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]

# Time Complexity  : O(m * n)
# Space Complexity : O(m * n)