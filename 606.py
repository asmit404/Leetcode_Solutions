"""
Title       : 606. Construct String from Binary Tree
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 08 Dec 2023
Solved Using    : Python3
"""

class Solution:
    def tree2str(self, root) -> str:
        if not root: return ""
        res = str(root.val)
        if root.left or root.right:
            res += "(" + self.tree2str(root.left) + ")"
        if root.right:
            res += "(" + self.tree2str(root.right) + ")"
        return res

# Time Complexity : O(n)
# Space Complexity : O(n)