"""
Title       : 1845. Seat Reservation Manager
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 06 Nov 2023
Solved Using    : Python3
"""

import heapq
class SeatManager:
    def __init__(self, n: int):
        self.last = 0
        self.pq = []

    def reserve(self) -> int:
        if self.pq:
            return heapq.heappop(self.pq)
        self.last += 1
        return self.last

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.pq, seatNumber)

# Time Complexity  : O(log(n))
# Space Complexity : O(n)