"""
Title       : 1207. Unique Number of Occurrences
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 17 Jan 2024
"""

from typing import List
from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return len(set(Counter(arr).values())) == len(Counter(arr).values())

# Time Complexity: O(N)
# Space Complexity: O(N)