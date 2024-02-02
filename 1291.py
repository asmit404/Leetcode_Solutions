"""
Title       : 1291. Sequential Digits
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 02 Feb 2024
"""

from typing import List
from bisect import insort

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        seq = '123456789'
        pool = []
        for i in range(len(seq)):
            for j in range(i+1, len(seq)+1):
                num = int(seq[i:j])
                if low <= num <= high:
                    insort(pool, num)
        return pool

# Time Complexity  : O(n ^ 2)
# Space Complexity : O(n)