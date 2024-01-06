"""
Title       : 1235. Maximum Profit in Job Scheduling
Difficulty  : Hard
Author      : Asmit Singh
Solved On   : 6 Jan 2024
"""

from typing import List
from bisect import bisect_right

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        n = len(jobs)
        endTimes = [e for s, e, p in jobs]

        dp = [0] * n
        dp[0] = jobs[0][2]

        for i, (s, e, p) in enumerate(jobs[1:], 1):
            dp[i] = dp[i - 1]

            index = bisect_right(endTimes, s) - 1
            dp[i] = max(dp[i], (dp[index] if index >= 0 else 0) + p)

        return dp[-1]

# Time Complexity  : O(n log n)
# Space Complexity : O(n)