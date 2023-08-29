"""
Title       : 2483. Minimum Penalty for a Shop
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 29 Aug 2023
Solved Using    : Python3
"""

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty = min_penalty = res = 0
        for i, ch in enumerate(customers):
            penalty += 1 if ch == "N" else -1
            if penalty < min_penalty:
                res, min_penalty = i + 1, penalty
        return res

# Time Complexity  : O(n)
# Space Complexity : O(1)