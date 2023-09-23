"""
Title       : 1048. Longest String Chain
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 23 Sept 2023
Solved Using    : Python3
"""

from typing import List

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        max_chain, dp = 0, {}
        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                prev_word = word[:i] + word[i+1:]
                if prev_word in dp:
                    dp[word] = max(dp[word], dp[prev_word] + 1)
            max_chain = max(max_chain, dp[word])
        return max_chain

# Time Complexity  : O(n * l^2)
# Space Complexity : O(n * l)