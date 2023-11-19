"""
Title       : 1887. Reduction Operations to Make the Array Elements Equal
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 19 Nov 2023
Solved Using    : Python3
"""

class Solution:
    def reductionOperations(self, nums) -> int:
        nums.sort()
        res = add = 0
        curr = nums[0]
        for num in nums:
            if num != curr:
                add += 1
                curr = num
            res += add
        return res

# Time Complexity  : O(nlogn)
# Space Complexity : O(1)