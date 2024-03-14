"""
Title       : 930. Binary Subarrays With Sum
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 14 Mar 2024
"""

class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        count = {0: 1}
        curr = res = 0
        for num in nums:
            curr += num
            if curr - goal in count:
                res += count[curr - goal]
            count[curr] = count.get(curr, 0) + 1
        return res

# Time Complexity  : O(n)
# Space Complexity : O(n)