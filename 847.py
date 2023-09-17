"""
Title       : 847. Shortest Path Visiting All Nodes
Difficulty  : Hard
Author      : Asmit Singh
Solved On   : 17 Sept 2023
Solved Using    : Python3
"""

from typing import List
from collections import deque

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        queue = deque([(1 << i, i, 0) for i in range(n)])
        visited = set((1 << i, i) for i in range(n))
        
        while queue:
            mask, node, dist = queue.popleft()
            if mask == (1 << n) - 1:
                return dist
            for neighbor in graph[node]:
                new_mask = mask | (1 << neighbor)
                if (new_mask, neighbor) not in visited:
                    visited.add((new_mask, neighbor))
                    queue.append((new_mask, neighbor, dist + 1))

# Time Complexity  : O(n * 2^n)
# Space Complexity : O(n * 2^n)