"""
Title       : 2385. Amount of Time for Binary Tree to Be Infected
Difficulty  : Medium
Author      : Asmit Singh
Solved On   :  10 Jan 2024
"""

class Solution:
    def amountOfTime(self, root, start) -> int:
        parent = {None: None}
        self.target = None
        self.res = 0
        vis = {None}

        def dfs(root, par):
            if root:
                parent[root] = par
                if root.val == start:
                    self.target = root
                dfs(root.left, root)
                dfs(root.right, root)
        dfs(root, None)

        def compute(root, x):
            if root not in vis:
                vis.add(root)
                self.res = max(self.res, x)
                compute(root.left, x+1)
                compute(root.right, x+1)
                compute(parent[root], x+1)
        compute(self.target, 0)

        return self.res

# Time Complexity  : O(n)
# Space Complexity : O(n)