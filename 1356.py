"""
Title       : 1356. Sort Integers by The Number of 1 Bits
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 30 Oct 2023
Solved Using    : Python3
"""

from typing import List
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))

# Time Complexity  : O(nlog(n))
# Space Complexity : O(n)