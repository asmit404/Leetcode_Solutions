"""
Title       : 2402. Most Booked Room
Difficulty  : Hard
Author      : Asmit Singh
Solved On   : 18 Feb 2024
"""

from typing import List
from heapq import heappop, heappush, heapify

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        freeRooms = [i for i in range(n)]
        pool, cnt = [], [0 for _ in range(n)]
        heapify(freeRooms)

        for s, e in meetings:
            while pool and pool[0][0] <= s:
                _, freeRoom = heappop(pool)
                heappush(freeRooms, freeRoom)
            room = -1
            if freeRooms:
                room = heappop(freeRooms)
                heappush(pool, (e, room))
            else:
                duration = e - s
                prev, room = heappop(pool)
                heappush(pool, (prev + duration, room))
            cnt[room] += 1

        return cnt.index(max(cnt))

# Time Complexity: O(nlogn)
# Space Complexity: O(n)