"""
Title       : 1282. Group the People Given the Group Size They Belong To
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 11 Sept 2023
Solved Using    : Python3
"""

from typing import List
from collections import defaultdict
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        hashmap = defaultdict(list)
        for i in range(len(groupSizes)):
            hashmap[groupSizes[i]].append(i)

        pool = []
        for v, arr in hashmap.items():
            temp = []
            for i in arr:
                if len(temp) < v:
                    temp.extend([i])
                if len(temp) == v:
                    pool.append(temp)
                    temp = []
        return pool

# Time Complexity  : O(n)
# Space Complexity : O(n)