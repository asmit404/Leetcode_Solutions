"""
Title       : 515. Find Largest Value in Each Tree Row
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 24 Oct 2023
Solved Using    : Python3
"""

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        pool = []
        queue = [root]
        while queue:
            pool.append(max(node.val for node in queue))
            queue = [child for node in queue for child in (node.left, node.right) if child]
        return pool

# Time Complexity  : O(n)
# Space Complexity : O(m)