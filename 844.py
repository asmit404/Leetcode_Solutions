"""
Title       : 844. Backspace String Compare
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 19 Oct 2023
Solved Using    : Python3
"""

from itertools import zip_longest
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x
        return all(x == y for x, y in zip_longest(helper(s), helper(t)))

# Time Complexity  : O(m + n)
# Space Complexity : O(m + n)