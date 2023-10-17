"""
Title       : 1361. Validate Binary Tree Nodes
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 17 Oct 2023
Solved Using    : Python3
"""

from typing import List
from collections import deque

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        root = 0
        children = set(leftChild + rightChild)
        for i in range(n):
            if i not in children:
                root = i
                break

        visited = [False] * n
        num = 0
        q = deque([root])
        while q:
            curr = q.popleft()
            if visited[curr]:
                return False

            visited[curr] = True
            num += 1

            for child in [leftChild[curr], rightChild[curr]]:
                if child != -1:
                    q.append(child)

        return num == n

# Time Complexity  : O(n)
# Space Complexity : O(n)