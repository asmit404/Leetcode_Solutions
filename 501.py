"""
Title       : 501. Find Mode in Binary Search Tree
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 01 Nov 2023
Solved Using    : Python3
"""

class Solution:
    def findMode(self, root):
        if not root: return []
        count = {}
        def inorder(node):
            if node:
                inorder(node.left)
                count[node.val] = count.get(node.val, 0) + 1
                inorder(node.right)
        inorder(root)
        max_count = max(count.values())
        return [k for k, v in count.items() if v == max_count]

# Time Complexity  : O(n)
# Space Complexity : O(n)