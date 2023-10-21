"""
Title       : 1425. Constrained Subsequence Sum
Difficulty  : Hard
Author      : Asmit Singh
Solved On   : 21 Oct 2023
Solved Using    : Python3
"""

from typing import List
from collections import deque

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dq = deque()
        for i in range(len(nums)):
            if dq:
                nums[i] += dq[0]
            while dq and dq[-1] < nums[i]:
                dq.pop()
            if nums[i] > 0:
                dq.append(nums[i])
            if dq and i >= k and dq[0] == nums[i-k]:
                dq.popleft()
        return max(nums)

# Beat 100% submissions in runtime.
# Time Complexity  : O(n)
# Space Complexity : O(k)