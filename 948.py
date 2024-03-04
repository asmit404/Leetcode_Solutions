"""
Title       : 948. Bag of Tokens
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 04 Mar 2024
"""

from collections import deque
class Solution:
    def bagOfTokensScore(self, tokens, P):
        tokens.sort()
        tokens = deque(tokens)
        res = 0
        while tokens:
            if P >= tokens[0]:
                P -= tokens.popleft()
                res += 1
            elif len(tokens) > 2 and res:
                P += tokens.pop()
                res -= 1
            else:
                return res
        return res

# Time Complexity: O(n log n)
# Space Complexity: O(n)