"""
Title       : 752. Open the Lock
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 22 Apr 2024
"""

from typing import List
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends: return -1
        queue = deque([('0000', 0)])
        visited = set('0000')
        while queue:
            curr, moves = queue.popleft()
            if curr == target: return moves
            for i in range(4):
                for j in [-1, 1]:
                    new_digit = (int(curr[i]) + j) % 10
                    new_combo = (curr[:i] + str(new_digit) + curr[i+1:])
                    if new_combo not in visited and new_combo not in deadends:
                        visited.add(new_combo)
                        queue.append((new_combo, moves + 1))
        return -1

# Time Complexity  : O(n)
# Space Complexity : O(n)