"""
Title       : 935. Knight Dialer
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 27 Nov 2023
Solved Using    : Python3
"""

class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 1000000007
        A, B, C, D = 1, 2, 4, 2
        if n == 1:
            return (A + B + C + D + 1)
        for _ in range(n - 1):
            A, B, C, D = B, (2 * A + C), (2 * B + 2 * D), C
        return (A + B + C + D) % MOD

# Time Complexity : O(n)
# Space Complexity : O(1)