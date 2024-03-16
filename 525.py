"""
Title       : 525. Contiguous Array
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 16 Mar 2024
"""

from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        curr_sum = curr_max = 0
        dic = {0: -1}
        for i in range(n):
            num = nums[i]
            curr_sum += (1 - 2 * num)
            if curr_sum not in dic:
                dic[curr_sum] = i
            else:
                curr_max = max(i - dic[curr_sum], curr_max)
        return curr_max

# Time Complexity  : O(n)
# Space Complexity : O(n)