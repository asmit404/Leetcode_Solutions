"""
Title       : 1971. Find if Path Exists in Graph
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 21 Apr 2024
"""

from typing import List
from collections import deque
from heapq import heappush

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination: return True
        if [source, destination] in edges: return True

        outedges = [list() for _ in range(n)]
        for s, e in edges:
            heappush(outedges[s], e)
            heappush(outedges[e], s)
        del edges

        vis = {source}
        pool = deque([source])
        while pool:
            node = pool.pop()
            vis.add(node)
            if node == destination:
                return True
            for dest in outedges[node]:
                if dest not in vis:
                    pool.append(dest)
        return False

# Time Complexity  : O(E + V)
# Space Complexity : O(E + V)