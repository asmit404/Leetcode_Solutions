"""
Title       : 279. Perfect Squares
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 08 Feb 2024
"""

from math import sqrt
class Solution:
    def numSquares(self, n: int) -> int:
        cache = {}
        def is_perfect_square(n):
            if n not in cache:
                square_root = int(sqrt(n))
                cache[n] = square_root**2 == n
            return cache[n]
        m = n
        if is_perfect_square(n): return 1
        while n & 3 == 0: n >>= 2
        if n & 7 == 7: return 4
        n = m
        for i in range(1, int(sqrt(n)) + 1):
            if is_perfect_square(n - i*i):
                return 2
        return 3

# Time complexity: O(sqrt(n))
# Space complexity: O(n)