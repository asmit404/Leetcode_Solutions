"""
Title       : 2265. Find Mode in Binary Search Tree
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 02 Nov 2023
Solved Using    : Python3
"""

class Solution:
    def averageOfSubtree(self, root):
        def traverse(node):
            if not node: return 0, 0, 0
            l_sum, l_count, l_res = traverse(node.left)
            r_sum, r_count, r_res = traverse(node.right)
            total = node.val + l_sum + r_sum
            count = 1 + l_count + r_count
            res = l_res + r_res + (total // count == node.val)
            return total, count, res
        return traverse(root)[2]

# Almost had to use my brain for this one.
# Time Complexity  : O(n)
# Space Complexity : O(n)