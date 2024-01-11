"""
Title       : 1026. Maximum Difference Between Node and Ancestor
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 11 Jan 2024
"""

class Solution:
    def maxAncestorDiff(self, root):
        return self.dfs(root, root.val, root.val)

    def dfs(self, node, min_val, max_val):
        if not node: return max_val - min_val
        min_val, max_val = min(min_val, node.val), max(max_val, node.val)
        return max(self.dfs(node.left, min_val, max_val), self.dfs(node.right, min_val, max_val))

# Time complexity: O(n)
# Space complexity: O(h)