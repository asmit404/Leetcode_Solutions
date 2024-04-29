"""
Title       : 2997. Minimum Number of Operations to Make Array XOR Equal to K
Difficulty  : Hard
Author      : Asmit Singh
Solved On   : 29 Apr 2024
"""

from typing import List
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = 0
        for n in nums:
            res = res ^ n
        return bin(res ^ k).count('1')

# Time Complexity  : O(n)
# Space Complexity : O(1)