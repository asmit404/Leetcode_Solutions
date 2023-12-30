"""
Title       : 1897. Redistribute Characters to Make All Strings Equal
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 30 Dec 2023
Solved Using    : Python3
"""

from typing import List
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        joint = ''.join(words)
        return all(joint.count(i) % len(words) == 0 for i in set(joint))

# Time Complexity  : O(nm^2)
# Space Complexity : O(k)