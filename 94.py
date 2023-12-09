"""
Title       : 94. Binary Tree Inorder Traversal
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 09 Dec 2023
Solved Using    : Python3
"""

class Solution:
    def inorderTraversal(self, root):
        res = []

        def helper(node):
            if node:
                helper(node.left)
                res.append(node.val)
                helper(node.right)
        helper(root)
        return res

# Time Complexity  : O(n)
# Space Complexity : O(n)