"""
Title       : 368. Largest Divisible Subset
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 09 Feb 2024
"""

from typing import List
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1] * n
        prev = [-1] * n
        max_size, max_index = 1, 0

        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
                    if dp[i] > max_size:
                        max_size = dp[i]
                        max_index = i

        pool = []
        while max_index != -1:
            pool.append(nums[max_index])
            max_index = prev[max_index]
        return pool[::-1]

# Time complexity: O(n ^ 2)
# Space complexity: O(n)