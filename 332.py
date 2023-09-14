"""
Title       : 332. Reconstruct Itinerary
Difficulty  : Hard
Author      : Asmit Singh
Solved On   : 14 Sept 2023
Solved Using    : Python3
"""

from collections import defaultdict
class Solution:
    def findItinerary(self, tickets):
        graph = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)
        itinerary = []
        def dfs(airport):
            while graph[airport]:
                dfs(graph[airport].pop())
            itinerary.append(airport)
        dfs("JFK")
        return itinerary[::-1]

# Time Complexity  : O(E log E)
# Space Complexity : O(E)