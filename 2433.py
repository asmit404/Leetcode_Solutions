"""
Title       : 2433. Find The Original Array of Prefix Xor
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 31 Oct 2023
Solved Using    : Python3
"""

from typing import List
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        return list(pref[i] ^ (pref[i-1] if i > 0 else 0) for i in range(len(pref)))

# Time Complexity  : O(n)
# Space Complexity : O(n)