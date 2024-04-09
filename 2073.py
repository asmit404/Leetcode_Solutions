"""
Title       : 2073. Time Needed to Buy Tickets
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 9 Apr 2024
"""

from typing import List
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        for i in range(len(tickets)):
            if i <= k:
                time += min(tickets[i], tickets[k])
            else:
                time += min(tickets[i], tickets[k] - 1)
        return time

# Time Complexity  : O(n)
# Space Complexity : O(1)