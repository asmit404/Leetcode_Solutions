"""
Title       : 1838. Frequency of the Most Frequent Element
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 18 Nov 2023
Solved Using    : Python3
"""

class Solution:
    def maxFrequency(self, nums, k) -> int:
        i = 0
        nums.sort()
        for j in range(len(nums)):
            k += nums[j]
            if k < nums[j] * (j-i+1):
                k -= nums[i]
                i += 1
        return j - i + 1

# Time Complexity  : O(nlogn)
# Space Complexity : O(1)