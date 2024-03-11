"""
Title       : 791. Custom Sort String
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 11 Mar 2024
"""

from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        cnt, pool = Counter(s), []
        for char in order:
            if char in cnt:
                pool.append(char * cnt[char])
                del cnt[char]
        for char, count in cnt.items():
            pool.append(char * count)
        return ''.join(pool)

# Time Complexity  : O(n + m)
# Space Complexity : O(n)