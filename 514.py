"""
Title       : 514. Freedom Trail
Difficulty  : Hard
Author      : Asmit Singh
Solved On   : 27 Apr 2024
"""

from collections import defaultdict
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        memo = {}
        pos = defaultdict(list)
        for i, c in enumerate(ring):
            pos[c].append(i)
        return self.compute(0, 0, pos, key, ring, memo)

    def compute(self, in_index, pos, positions, key, ring, memo):
        if in_index == len(key):
            return 0
        res = float('inf')
        if (in_index, pos) in memo:
            return memo[(in_index, pos)]
        for i in positions[key[in_index]]:
            if i >= pos:
                steps = min(i - pos, pos + len(ring) - i)
            else:
                steps = min(pos - i, i + len(ring) - pos)
            res = min(res, steps + self.compute(in_index +
                      1, i, positions, key, ring, memo))
        result = res + 1
        memo[(in_index, pos)] = result
        return result

# Time Complexity  : O(n ^ 2 * m)
# Space Complexity : O(n * m)