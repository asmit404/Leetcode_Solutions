"""
Title       : 2962. Count Subarrays Where Max Element Appears at Least K Times
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 29 Mar 2024
"""

from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        high = max(nums)
        cnt = res = left = 0
        for right in range(n):
            if nums[right] == high:
                cnt += 1
            while cnt >= k:
                res += n - right
                if nums[left] == high:
                    cnt -= 1
                left += 1
        return res

# Time Complexity  : O(n)
# Space Complexity : O(1)