"""
Title       : 1910. Remove All Occurrences of a Substring
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 11 Feb 2025
"""

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s = s.replace(part, "", 1)
        return s

# Beats 100% of submissions in runtime
# Time Complexity: O(n)
# Space Complexity: O(n)