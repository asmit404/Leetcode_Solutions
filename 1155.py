"""
Title       : 1155. Number of Dice Rolls With Target Sum
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 26 Dec 2023
Solved Using    : Python3
"""

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if target < n: return 0
        if target == n: return 1
        if target == n*k: return 1
        if target > n*k: return 0

        MOD = 1000000007
        ways = [0]*(target+1)
        ways[0] = 1

        for _ in range(n):
            total = sum(ways[t] for t in range(max(target-k, 0), target)) % MOD
            ways[target] = total
            for t in range(target-1, -1, -1):
                if t-k >= 0:
                    total += ways[t-k]
                total -= ways[t]
                ways[t] = total

        return ways[target] % MOD

# Beats 100% of users in runtime
# Time Complexity  : O(n * k)
# Space Complexity : O(target)