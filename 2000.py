"""
Title       : 2000. Reverse Prefix of Word
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 1 May 2024
"""

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = word.find(ch)
        return word[:index+1][::-1] + word[index+1:] if index != -1 else word

# Time Complexity  : O(n)
# Space Complexity : O(n)