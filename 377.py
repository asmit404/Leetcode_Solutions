"""
Title       : 377. Combination Sum IV
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 9 Sept 2023
Solved Using    : Python3
"""

from typing import List
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        return dp[-1]

# Time Complexity  : O(n * target)
# Space Complexity : O(target)