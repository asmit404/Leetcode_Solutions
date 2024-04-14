"""
Title       : 404. Sum of Left Leaves
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 14 Apr 2024
"""

class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        def compute(root, is_left):
            if root is None: return 0
            if root.left is None and root.right is None: return root.val if is_left else 0
            return compute(root.left, True) + compute(root.right, False)
        return compute(root, False)

# Ah yes, 404
# Time Complexity  : O(n)
# Space Complexity : O(h)