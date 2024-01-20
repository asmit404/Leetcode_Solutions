"""
Title       : 907. Sum of Subarray Minimums
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 20 Jan 2024
"""

from typing import List
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 1000000007
        res, stack = 0, [-1]
        arr.append(0)
        for i in range(len(arr)):
            while arr[i] < arr[stack[-1]]:
                idx = stack.pop()
                res += arr[idx]*(i - idx)*(idx - stack[-1])
            stack.append(i)
        return res % MOD

# Time Complexity: O(n)
# Space Complexity: O(n)