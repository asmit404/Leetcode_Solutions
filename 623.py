"""
Title       : 623. Add One Row to Tree
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 16 Apr 2024
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            out = TreeNode(val)
            out.left = root
            return out
        def compute(tree, d):
            if not tree: return
            if d == depth-1:
                tree.left = TreeNode(val, tree.left)
                tree.right = TreeNode(val, None, tree.right)
                return
            if d < depth-1:
                compute(tree.left, d+1)
                compute(tree.right, d+1)
        compute(root, 1)
        return root

# Time Complexity  : O(n)
# Space Complexity : O(h)