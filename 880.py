"""
Title       : 880. Decoded String at Index
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 27 Sept 2023
Solved Using    : Python3
"""

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0
        for char in s:
            if char.isdigit():
                size *= int(char)
            else:
                size += 1
        for char in reversed(s):
            k %= size
            if k == 0 and char.isalpha():
                return char
            if char.isdigit():
                size //= int(char)
            else:
                size -= 1

# Time Complexity  : O(n)
# Space Complexity : O(1)