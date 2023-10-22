"""
Title       : 1793. Maximum Score of a Good Subarray
Difficulty  : Hard
Author      : Asmit Singh
Solved On   : 22 Oct 2023
Solved Using    : Python3
"""

from typing import List
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        l = r = k
        min_val = res = nums[k]
        while l > 0 or r < len(nums) - 1:
            if (nums[l-1] if l else 0) >= (nums[r+1] if r < len(nums) - 1 else 0):
                l -= 1
            else:
                r += 1
            min_val = min(min_val, nums[l], nums[r])
            res = max(res, min_val * (r - l + 1))
        return res

# Time Complexity  : O(n)
# Space Complexity : O(1)