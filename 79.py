"""
Title       : 79. Word Search
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 3 Apr 2024
"""

from typing import List
from collections import Counter

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        vis = [[False] * len(board[i]) for i in range(len(board))]
        cnt = Counter(word)

        def dfs(i, j, idx):
            if idx == len(word):
                return True
            if i < 0 or i == len(board) or j < 0 or j == len(board[i]):
                return False
            if vis[i][j]:
                return False
            if board[i][j] == word[idx]:
                vis[i][j] = True
                if dfs(i - 1, j, idx + 1) or dfs(i + 1, j, idx + 1) or dfs(i, j - 1, idx + 1) or dfs(i, j + 1, idx + 1):
                    return True
                vis[i][j] = False
            return False

        if cnt[word[-1]] < cnt[word[0]]:
            word = word[::-1]

        for i in range(len(board)):
            for j in range(len(board[i])):
                if dfs(i, j, 0):
                    return True
        return False

# Time Complexity  : O(n * 4^l)
# Space Complexity : O(L)