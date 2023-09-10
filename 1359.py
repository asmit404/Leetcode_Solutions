"""
Title       : 1359. Count All Valid Pickup and Delivery Options
Difficulty  : Hard
Author      : Asmit Singh
Solved On   : 10 Sept 2023
Solved Using    : Python3
"""

class Solution:
    def countOrders(self, n: int) -> int:
        count, mod = 1, 10**9 + 7
        for i in range(2, n + 1):
            count = count * (i * 2 - 1) * (i * 2) // 2 % mod
        return count

# Time Complexity  : O(n)
# Space Complexity : O(1)