"""
Title       : 815. Bus Routes
Difficulty  : Hard
Author      : Asmit Singh
Solved On   : 12 Nov 2023
Solved Using    : Python3
"""

class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0

        m = max(max(rt) for rt in routes)
        if m < target:
            return -1

        n = len(routes)
        min_b = [float('inf')] * (m + 1)
        min_b[source] = 0

        flag = True
        while flag:
            flag = False
            for rt in routes:
                mi = float('inf')
                for st in rt:
                    mi = min(mi, min_b[st])
                mi += 1
                for st in rt:
                    if min_b[st] > mi:
                        min_b[st] = mi
                        flag = True

        return min_b[target] if min_b[target] < float('inf') else -1

# Time Complexity  : O(n^2 * m)
# Space Complexity : O(m)