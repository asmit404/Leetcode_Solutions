"""
Title       : 823. Binary Trees With Factors
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 26 Oct 2023
Solved Using    : Python3
"""

from typing import List

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        arr.sort()
        s = set(arr)
        dp = {x: 1 for x in arr}
        
        for i in arr:
            for j in arr:
                if j > i**0.5:
                    break
                if i % j == 0 and i // j in s:
                    if i // j == j:
                        dp[i] += dp[j] * dp[j]
                    else:
                        dp[i] += dp[j] * dp[i // j] * 2
                    dp[i] %= MOD
        
        return sum(dp.values()) % MOD

# Time Complexity  : O(n^2)
# Space Complexity : O(n)