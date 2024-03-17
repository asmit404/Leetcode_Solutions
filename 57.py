"""
Title       : 57. Insert Interval
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 17 Mar 2024
"""

from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        size, res, i = len(intervals), [], 0
        while i < size and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        while i < size and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        res.append(newInterval)

        while i < size:
            res.append(intervals[i])
            i += 1
        return res

# Time Complexity  : O(n)
# Space Complexity : O(n)