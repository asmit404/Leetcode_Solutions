"""
Title       : 1921. Eliminate Maximum Number of Monsters
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 07 Nov 2023
Solved Using    : Python3
"""

from math import ceil
from operator import truediv

class Solution:
    def eliminateMaximum(self, dist, speed):
        time = sorted(list(map(truediv, dist, speed)))
        for idx, t in enumerate(time):
            if idx >= ceil(t):
                return idx
        return idx + 1

# Fun Question.
# Time Complexity  : O(nlog(n))
# Space Complexity : O(n)