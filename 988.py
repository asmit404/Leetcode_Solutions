"""
Title       : 988. Smallest String Starting From Leaf
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 17 Apr 2024
"""

class Solution:
    def smallestFromLeaf(self, root) -> str:
        res = ["z" * 30]
        def compute(r, s):
            if not r: return
            if not r.left and not r.right:
                x = s + chr(r.val+97)
                x = x[::-1]
                res[0] = min(res[0], x)
            compute(r.left, s + chr(r.val + 97))
            compute(r.right, s + chr(r.val + 97))
        compute(root, "")
        return res[0]

# Time Complexity  : O(n)
# Space Complexity : O(h)