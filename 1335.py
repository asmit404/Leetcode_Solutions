"""
Title       : 1335. Minimum Difficulty of a Job Schedule
Difficulty  : Hard
Author      : Asmit Singh
Solved On   : 29 Dec 2023
Solved Using    : Python3
"""

class Solution:
    def minDifficulty(self, jobDifficulty, d):
        n = len(jobDifficulty)
        if n < d: return -1
        dp = [[float('inf')] * n + [0] for _ in range(d + 1)]
        for day in range(1, d + 1):
            for i in range(day - 1, n):
                m = 0
                for j in range(i, day - 2, -1):
                    m = max(m, jobDifficulty[j])
                    dp[day][i] = min(dp[day][i], dp[day - 1][j - 1] + m)
        return dp[d][n - 1]

# Time Complexity  : O(n ^ 2 * d)
# Space Complexity : O(n * d)