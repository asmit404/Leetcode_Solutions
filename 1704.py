"""
Title       : 1704. Determine if String Halves Are Alike
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 12 Jan 2024
"""

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        pool = set("aeiouAEIOU")
        return sum(c in pool for c in s[:len(s)//2]) == sum(c in pool for c in s[len(s)//2:])

# Time complexity: O(n)
# Space complexity: O(1)