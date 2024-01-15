"""
Title       : 2225. Find Players With Zero or One Losses
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 15 Jan 2024
"""

from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        zero_loss, one_loss, more_losses  = set(), set(), set()
        for winner, loser in matches:
            if winner not in one_loss and winner not in more_losses:
                zero_loss.add(winner)
            if loser in zero_loss:
                zero_loss.remove(loser)
                one_loss.add(loser)
            elif loser in one_loss:
                one_loss.remove(loser)
                more_losses.add(loser)
            elif loser not in one_loss and loser not in more_losses:
                one_loss.add(loser)
        return [sorted(list(zero_loss)), sorted(list(one_loss))]

# Time Complexity: O(n log n)
# Space Complexity: O(n)