"""
Title       : 1915. Number of Wonderful Substrings
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 30 Apr 2024
"""

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = [1] + [0] * 1024
        cur = res = 0
        for c in word:
            cur ^= 1 << (ord(c) - ord("a"))
            res += count[cur]
            for i in range(10):
                res += count[cur ^ (1 << i)]
            count[cur] += 1
        return res

# Time Complexity  : O(n)
# Space Complexity : O(1)