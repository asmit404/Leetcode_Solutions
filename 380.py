"""
Title       : 380. Insert Delete GetRandom O(1)
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 16 Jan 2024
"""

import random
class RandomizedSet:
    def __init__(self):
        self.pool = []
        self.hmap = {}

    def search(self, val):
        return val in self.hmap

    def insert(self, val):
        if self.search(val):
            return False

        self.pool.append(val)
        self.hmap[val] = len(self.pool) - 1
        return True

    def remove(self, val):
        if not self.search(val):
            return False

        idx, last = self.hmap[val], self.pool[-1]
        self.pool[idx] = last
        if idx != len(self.pool) - 1:
            self.hmap[last] = idx
        self.pool.pop()
        del self.hmap[val]
        return True

    def getRandom(self):
        return random.choice(self.pool)

# Time Complexity: O(1)
# Space Complexity: O(N)