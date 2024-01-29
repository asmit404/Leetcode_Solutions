"""
Title       : 232. Implement Queue using Stacks
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 29 Jan 2024
"""

class MyQueue:
    def __init__(self):
        self.pool = []

    def push(self, x: int) -> None:
        self.pool.append(x)

    def pop(self) -> int:
        return self.pool.pop(0)

    def peek(self) -> int:
        return self.pool[0]

    def empty(self) -> bool:
        return len(self.pool) == 0

# Time Complexity  : O(n)
# Space Complexity : O(n)