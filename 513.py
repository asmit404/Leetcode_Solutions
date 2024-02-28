"""
Title       : 513. Find Bottom Left Tree Value
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 28 Feb 2024
"""

from collections import deque
class Solution:
    def findBottomLeftValue(self, root) -> int:
        queue = deque([root])
        res = None
        while queue:
            node = queue.popleft()
            res = node.val
            if node.right: queue.append(node.right)
            if node.left: queue.append(node.left)
        return res

# Time Complexity: O(n)
# Space Complexity: O(n)