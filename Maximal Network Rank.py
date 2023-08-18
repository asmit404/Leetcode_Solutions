"""
Title       : 1615. Maximal Network Rank
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 18 Aug 2023
Solved Using    : Python3
"""

import heapq
from typing import List
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        degrees = [0] * n
        for u, v in roads:
            degrees[u] += 1
            degrees[v] += 1

        max_deg, second_max_deg = heapq.nlargest(2, degrees)
        max_count = degrees.count(max_deg)
        second_max_count = degrees.count(second_max_deg)

        if max_count > 1:
            directly_connected = sum(1 for u, v in roads if degrees[u] == max_deg and degrees[v] == max_deg)
            possible_connections = max_count * (max_count - 1) // 2
            result = 2 * max_deg - 1 if possible_connections == directly_connected else 2 * max_deg
        else:
            direct_connections_to_second = sum(1 for u, v in roads if degrees[u] + degrees[v] == max_deg + second_max_deg)
            result = max_deg + second_max_deg - \
                1 if second_max_count == direct_connections_to_second else max_deg + second_max_deg

        return result

# Time Complexity : O(n + m log n)
# Space Complexity : O(n)