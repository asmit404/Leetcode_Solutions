"""
Title       : 310. Minimum Height Trees
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 23 Apr 2024
"""

from typing import List
from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        pool = defaultdict(list)
        degree = [0] * n
        for u, v in edges:
            pool[u].append(v)
            pool[v].append(u)
            degree[u] += 1
            degree[v] += 1

        leaves = deque([i for i in range(n) if degree[i] == 1])
        rem_nodes = n
        while rem_nodes > 2:
            leaves_count = len(leaves)
            rem_nodes -= leaves_count
            for _ in range(leaves_count):
                leaf = leaves.popleft()
                for neighbor in pool[leaf]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        leaves.append(neighbor)
        return list(leaves)

# Time Complexity  : O(n)
# Space Complexity : O(n)