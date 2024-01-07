"""
Title       : 446. Arithmetic Slices II - Subsequence
Difficulty  : Hard
Author      : Asmit Singh
Solved On   : 7 Jan 2024
"""

from typing import List
from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = [defaultdict(int) for _ in nums]
        total = 0
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += dp[j][diff] + 1
                if diff in dp[j]:
                    total += dp[j][diff]
        return total

# Time Complexity  : O(n^2)
# Space Complexity : O(n^2)