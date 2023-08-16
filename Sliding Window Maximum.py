"""
Title       : 239. Sliding Window Maximum
Difficulty  : Hard
Author      : Asmit Singh
Solved On   : 16 Aug 2023
Solved Using    : Python3
"""

import collections
class Solution:
    def maxSlidingWindow(self, nums, k):
        d = collections.deque()
        pool = []
        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()
            d.append(i)
            if d[0] == i - k:
                d.popleft()
            if i >= k - 1:
                pool.append(nums[d[0]])
        return pool

# Time Complexity : O(n)
# Space Complexity : O(k)