"""
Title       : 977. Squares of a Sorted Array
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 02 Mar 2024
"""

class Solution(object):
    def sortedSquares(self, nums):
        squares = [num * num for num in nums]
        return sorted(squares)

# Time Complexity: O(n log n)
# Space Complexity: O(n)