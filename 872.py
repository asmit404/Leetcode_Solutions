"""
Title       : 872. Leaf-Similar Trees
Difficulty  : Easy
Author      : Asmit Singh
Solved On   :  9 Jan 2024
"""

class Solution:
    def leafSimilar(self, root1, root2) -> bool:
        def compute(root, leaf_values):
            if not root: return
            if not root.left and not root.right:
                leaf_values.append(root.val)
            compute(root.left, leaf_values)
            compute(root.right, leaf_values)

        pool1, pool2 = [], []
        compute(root1, pool1)
        compute(root2, pool2)
        return pool1 == pool2

# Time Complexity  : O(n)
# Space Complexity : O(n)