"""
Title       : 58. Length of Last Word
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 1 Apr 2024
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.rstrip().split(' ')
        return len(words[-1]) if words else 0

# Time Complexity  : O(n)
# Space Complexity : O(n)