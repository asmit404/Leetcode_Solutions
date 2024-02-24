"""
Title       : 2092. Find All People With Secret
Difficulty  : Hard
Author      : Asmit Singh
Solved On   : 24 Feb 2024
"""

from typing import List
from collections import defaultdict, deque

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key = lambda x: x[2])
        res = set()
        res.add(0)
        res.add(firstPerson)
        hmap = defaultdict(list)

        for p1, p2, time in meetings:
            hmap[time].append([p1, p2])

        for time, timeSlots in hmap.items():
            graph = defaultdict(list)
            curSecrets = set()
            for p1, p2 in timeSlots:
                graph[p1].append(p2)
                graph[p2].append(p1)

                if p1 in res:
                    curSecrets.add(p1)
                if p2 in res:
                    curSecrets.add(p2)

            dq = deque(curSecrets)
            while dq:
                for _ in range(len(dq)):
                    cur = dq.popleft()
                    for nei in graph[cur]:
                        if nei not in res:
                            res.add(nei)
                            dq.append(nei)
        return res

# Time Complexity: O(nlogn + n)
# Space Complexity: O(n)