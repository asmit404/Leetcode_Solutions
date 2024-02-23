"""
Title       : 787. Cheapest Flights Within K Stops
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 23 Feb 2024
"""

from typing import List
from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(dict)
        for u, v, w in flights:
            graph[u][v] = w
        minHeap = [(0, src, 0)]
        vis = [float('inf')] * n

        while minHeap:
            currCost, currNode, currSteps = heappop(minHeap)
            if currNode == dst: return currCost
            if currSteps > k or currSteps >= vis[currNode]: continue
            vis[currNode] = currSteps
            for neighbor, price in graph[currNode].items():
                heappush(minHeap, (currCost + price, neighbor, currSteps + 1))
        return -1

# Time Complexity: O(nlogn)
# Space Complexity: O(n)