"""
Title       : 950. Reveal Cards In Increasing Order
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 10 Apr 2024
"""

from typing import List
from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        pool = deque()
        for card in reversed(sorted(deck)):
            pool.rotate()
            pool.appendleft(card)
        return list(pool)

# Time Complexity  : O(n log n)
# Space Complexity : O(n)