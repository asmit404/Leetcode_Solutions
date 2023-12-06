"""
Title       : 1716. Calculate Money in Leetcode Bank
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 06 Dec 2023
Solved Using    : Python3
"""

class Solution:
    def totalMoney(self, n: int) -> int:
        weeks, days = divmod(n, 7)
        weekTotal = 28 * weeks + 7 * weeks * (weeks - 1) // 2
        dayTotal = days * (days + 1) // 2 + weeks * days
        return weekTotal + dayTotal

# Time Complexity : O(1)
# Space Complexity : O(1)