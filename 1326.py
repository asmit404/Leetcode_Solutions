"""
Title       : 1326. Minimum Number of Taps to Open to Water a Garden
Difficulty  : Hard
Author      : Asmit Singh
Solved On   : 31 Aug 2023
Solved Using    : Python3
"""

from typing import List
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        coverage = [0] * (n + 1)
        for i, r in enumerate(ranges):
            if r == 0:
                continue
            left = max(0, i - r)
            coverage[left] = max(coverage[left], i + r)

        end, far_can_reach, tap_count = 0, 0, 0
        for i, reach in enumerate(coverage):
            if i > end:
                if far_can_reach <= end:
                    return -1
                end, tap_count = far_can_reach, tap_count + 1
            far_can_reach = max(far_can_reach, reach)

        return tap_count + (end < n)

# Time Complexity  : O(n)
# Space Complexity : O(n)