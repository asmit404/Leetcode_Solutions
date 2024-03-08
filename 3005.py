"""
Title       : 3005. Count Elements With Maximum Frequency
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 08 Mar 2024
"""

from typing import List
from collections import defaultdict, Counter

class Solution:
    def maxFrequencyElements(self, numbers: List[int]) -> int:
        freq_count = defaultdict(int)
        for count in Counter(numbers).values():
            freq_count[count] += 1
        max_freq = max(freq_count)
        return max_freq * freq_count[max_freq]

# Time Complexity  : O(n)
# Space Complexity : O(n)