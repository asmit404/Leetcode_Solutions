"""
Title       : 834. Sum of Distances in Tree
Difficulty  : Hard
Author      : Asmit Singh
Solved On   : 28 Apr 2024
"""

from typing import List
from collections import defaultdict

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph, count, res = defaultdict(list), [1] * n, [0] * n
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, parent, pass2):
            nonlocal count, res
            for child in graph[node]:
                if child != parent:
                    if not pass2:
                        dfs(child, node, 0)
                        count[node] += count[child]
                        res[node] += res[child] + count[child]
                    else:
                        res[child] = res[node] - \
                            count[child] + (n - count[child])
                        dfs(child, node, 1)

        dfs(0, -1, 0)
        dfs(0, -1, 1)
        return res

# Time Complexity  : O(n)
# Space Complexity : O(n)