"""
Title       : 1743. Restore the Array From Adjacent Pairs
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 10 Nov 2023
Solved Using    : Python3
"""

from typing import List
from collections import defaultdict

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adjacent = defaultdict(list)
        for u, v in adjacentPairs:
            adjacent[u].append(v)
            adjacent[v].append(u)

        array = []
        for num, neighbours in adjacent.items():
            if len(neighbours) == 1:
                array.extend([num, neighbours[0]])
                break

        n = len(adjacentPairs) + 1
        while len(array) < n:
            u, v = adjacent[array[-1]]
            array.append(v if array[-2] != v else u)
        return array

# Time Complexity  : O(n)
# Space Complexity : O(n)