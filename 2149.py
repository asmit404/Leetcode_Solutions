"""
Title       : 2149. Rearrange Positive and Negative Numbers
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 14 Feb 2024
"""

from typing import List
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        v1 = [num for num in nums if num > 0]
        v2 = [num for num in nums if num <= 0]
        return [num for pair in zip(v1, v2) for num in pair]

# Time complexity: O(n)
# Space complexity: O(n)