"""
Title       : 1544. Make The String Great
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 5 Apr 2024
"""

class Solution:
    def makeGood(self, s: str) -> str:
        pool = []
        for char in s:
            if pool and abs(ord(char) - ord(pool[-1])) == 32:
                pool.pop()
            else:
                pool.append(char)
        return ''.join(pool)

# Time Complexity  : O(n)
# Space Complexity : O(n)