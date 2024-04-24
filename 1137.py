"""
Title       : 1137. N-th Tribonacci Number
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 24 Apr 2024
"""

class Solution:
    def tribonacci(self, n: int) -> int:
        pool = [0, 1, 1]
        if n <= 2:
            return pool[n]
        else:
            for _ in range(3, n + 1):
                pool.append(pool[-1] + pool[-2] + pool[-3])
            return pool[-1]

# Time Complexity  : O(n)
# Space Complexity : O(n)