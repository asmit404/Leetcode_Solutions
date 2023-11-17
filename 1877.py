"""
Title       : 1877. Minimize Maximum Pair Sum in Array
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 17 Nov 2023
Solved Using    : Python3
"""

class Solution:
    def minPairSum(self, nums) -> int:
        nums.sort()
        max_sum, ptr1, ptr2 = 0 , 0, len(nums) - 1
        while ptr1 < ptr2:
            max_sum = max(max_sum, nums[ptr1] + nums[ptr2])
            ptr1 += 1
            ptr2 -= 1
        return max_sum

# Time Complexity  : O(nlogn)
# Space Complexity : O(1)