"""
Title       : 42. Trapping Rain Water
Difficulty  : Hard
Author      : Asmit Singh
Solved On   : 12 Apr 2024
"""

from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        i = res = 0
        j = len(height) - 1
        lMax, rMax = height[0], height[j]
        while i < j:
            if lMax <= rMax:
                res += lMax - height[i]
                i += 1
                lMax = max(lMax, height[i])
            else:
                res += rMax - height[j]
                j -= 1
                rMax = max(rMax, height[j])
        return res

# Time Complexity  : O(n)
# Space Complexity : O(1)