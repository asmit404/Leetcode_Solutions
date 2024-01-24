"""
Title       : 1457. Pseudo-Palindromic Paths in a Binary Tree
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 24 Jan 2024
"""

class Solution:
    def pseudoPalindromicPaths(self, root):
        pool, cnt = [(root, 0)], 0
        while pool:
            node, path = pool.pop()
            if node:
                path ^= 1 << node.val
                if not node.left and not node.right:
                    if path & (path - 1) == 0:
                        cnt += 1
                else:
                    pool.append((node.right, path))
                    pool.append((node.left, path))
        return cnt

# Time Complexity  : O(n)
# Space Complexity : O(h)