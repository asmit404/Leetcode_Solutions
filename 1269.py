"""
Title       : 1269. Number of Ways to Stay in the Same Place After Some Steps
Difficulty  : Hard
Author      : Asmit Singh
Solved On   : 15 Oct 2023
Solved Using    : Python3
"""

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        arrLen = min(steps // 2 + 1, arrLen)
        dp = [0] * arrLen
        dp[0] = 1
        MOD = 10 ** 9 + 7
        for step in range(1, steps + 1):
            new_dp = [0] * arrLen
            for i in range(min(arrLen, steps - step + 1)):
                new_dp[i] = dp[i] + (dp[i - 1] if i > 0 else 0) + (dp[i + 1] if i + 1 < arrLen else 0)
            dp = new_dp
        return dp[0] % MOD

# Beat 100% submissions in runtime.
# Time Complexity  : O(n^2)
# Space Complexity : O(n)