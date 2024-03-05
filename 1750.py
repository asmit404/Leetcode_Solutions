"""
Title       : 1750. Minimum Length of String After Deleting Similar Ends
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 05 Mar 2024
"""

class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1
        while left < right and s[left] == s[right]:
            char = s[left]
            left += 1
            right -= 1
            while left <= right and s[left] == char:
                left += 1
            while left <= right and s[right] == char:
                right -= 1
        return right - left + 1

# Time Complexity: O(n)
# Space Complexity: O(1)