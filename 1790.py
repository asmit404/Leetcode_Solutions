"""
Title       : 1790. Check if One String Swap Can Make Strings Equal
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 5 Feb 2025
"""

class Solution():
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff = [(a, b) for a, b in zip(s1, s2) if a != b]
        if not diff: return True
        if len(diff) == 2 and diff[0] == diff[1][::-1]: return True
        return False

# Beats 100% of submissions in runtime
# Time Complexity: O(n)
# Space Complexity: O(n)