"""
Title       : 225. Implement Stack using Queues
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 28 Aug 2023
Solved Using    : Python3
"""

from collections import deque
class MyStack:
    def __init__(self): self.q = deque()

    def push(self, x: int) -> None:
        temp = deque([x])
        temp.extend(self.q)
        self.q = temp

    def pop(self) -> int: return self.q.popleft()
    def top(self) -> int: return self.q[0]
    def empty(self) -> bool: return len(self.q) == 0

# Nice Question, I like it.
# Time Complexity  : O(1)
# Space Complexity : O(n)