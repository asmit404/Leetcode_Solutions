"""
Title       : 1220. Count Vowels Permutation
Difficulty  : Hard
Author      : Asmit Singh
Solved On   : 28 Oct 2023
Solved Using    : Python3
"""

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        a = e = i = o = u = 1
        for _ in range(1, n):
            a, e, i, o, u = e, (a + i) % MOD, (a + e + o + u) % MOD, (i + u) % MOD, a
        return sum([a, e, i, o, u]) % MOD

# Time Complexity  : O(n)
# Space Complexity : O(1)