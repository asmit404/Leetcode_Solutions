"""
Title       : 129. Sum Root to Leaf Numbers
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 15 Apr 2024
"""

class Solution:
    def sumNumbers(self, root) -> int:
        def compute(node, curr = 0):
            if not node: return 0
            curr = curr * 10 + node.val
            if not node.left and not node.right:
                return curr
            return compute(node.left, curr) + compute(node.right, curr)
        return compute(root)

# Time Complexity  : O(n)
# Space Complexity : O(h)