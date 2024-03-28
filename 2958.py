"""
Title       : 2958. Length of Longest Subarray With at Most K Frequency
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 28 Mar 2024
"""

from typing import List
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        hmap = {}
        res = right = left = 0
        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1
            if hmap[num] > k:
                res = max(res, right - left)
                while nums[left] != nums[right]:
                    hmap[nums[left]] -= 1
                    left += 1
                hmap[nums[left]] -= 1
                left += 1
            right += 1
        res = max(res, right - left)
        return res

# Time Complexity  : O(n)
# Space Complexity : O(n)