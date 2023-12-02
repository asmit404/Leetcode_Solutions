"""
Title       : 1160. Find Words That Can Be Formed by Characters
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 02 Dec 2023
Solved Using    : Python3
"""

from typing import List
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        pool = []
        for word in words:
            for char in word:
                if chars.count(char) < word.count(char):
                    break
            else:
                pool.append(len(word))
        return sum(pool)

# Time Complexity : O(n^2)
# Space Complexity : O(n)