"""
Title       : 2706. Buy Two Chocolates
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 20 Dec 2023
Solved Using    : Python3
"""

from typing import List
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        total = prices[0] + prices[1]
        return money if total > money else money - total

# Time Complexity  : O(n log n)
# Space Complexity : O(1)