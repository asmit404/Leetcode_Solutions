"""
Title       : 938. Range Sum of BST
Difficulty  : Easy
Author      : Asmit Singh
Solved On   :  8 Jan 2024
"""

class Solution:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        def dfs(node): 
            return 0 if not node else ((low <= node.val <= high) * node.val) + \
            dfs(node.left) * (low < node.val) + \
            dfs(node.right) * (node.val < high)
        return dfs(root)

# Had fun solving this one.
# Time Complexity  : O(n)
# Space Complexity : O(h)