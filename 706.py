"""
Title       : 706. Design HashMap
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 4 Oct 2023
Solved Using    : Python3
"""

class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.data = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key: int, val: int) -> None:
        h = self._hash(key)
        for i, (k, v) in enumerate(self.data[h]):
            if k == key:
                self.data[h][i] = (key, val)
                return
        self.data[h].append((key, val))

    def get(self, key: int) -> int:
        h = self._hash(key)
        for k, v in self.data[h]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        h = self._hash(key)
        for i, (k, v) in enumerate(self.data[h]):
            if k == key:
                del self.data[h][i]
                return

# Time Complexity  : O(n/k)
# Space Complexity : O(n)