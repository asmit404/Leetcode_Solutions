"""
Title       : 1043. Partition Array for Maximum Sum
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 03 Feb 2024
"""

from typing import List
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n+1)
        for i in range(n):
            currMax = 0
            for j in range(i, max(-1, i-k), -1):
                currMax = max(currMax, arr[j])
                dp[i+1] = max(dp[i+1], currMax * (i-j+1) + dp[j])
        return dp[-1]

# Time Complexity  : O(n * k)
# Space Complexity : O(n)