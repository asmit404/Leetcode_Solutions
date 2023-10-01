"""
Title       : 557. Reverse Words in a String III
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 1 Oct 2023
Solved Using    : Python3
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reversed_words = map(lambda word: word[::-1], words)
        return ' '.join(reversed_words)

# Time Complexity  : O(n)
# Space Complexity : O(n)