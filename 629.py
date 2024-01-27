"""
Title       : 629. K Inverse Pairs Array
Difficulty  : Hard
Author      : Asmit Singh
Solved On   : 27 Jan 2024
"""

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 1000000007
        if k == 0: return 1
        if n == 1: return 1 if k == 0 else 0

        curr = [0] * (k + 1)
        curr[0] = 1
        prev = [0] * (k + 1)

        for i in range(n - 2, -1, -1):
            cnt, thold = 0, n - i
            for j in range(0, k + 1):
                cnt += curr[j]
                if j >= thold:
                    cnt -= curr[j - thold]
                cnt %= MOD
                prev[j] = cnt
            curr, prev = prev, curr

        return curr[k]

# Time Complexity  : O(n * k)
# Space Complexity : O(k)