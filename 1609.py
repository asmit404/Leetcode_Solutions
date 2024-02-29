"""
Title       : 1609. Even Odd Tree
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 29 Feb 2024
"""

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        pool = deque([root])
        rem = 1
        while pool:
            l = len(pool)
            n = pool.popleft()
            if n.val % 2 != rem: 
                return False
            p = n.val

            if n.left:
                pool.append(n.left)
            if n.right:
                pool.append(n.right)

            for _ in range(l-1):
                n = pool.popleft()
                if n.val % 2 != rem: 
                    return False
                if rem:
                    if p >= n.val:
                        return False
                else:
                    if n.val >= p:
                        return False

                p = n.val
                if n.left:
                    pool.append(n.left)
                if n.right:
                    pool.append(n.right)
            rem ^= 1
        return True

# Time Complexity: O(n)
# Space Complexity: O(n)