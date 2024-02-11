"""
Title       : 1463. Cherry Pickup II
Difficulty  : Hard
Author      : Asmit Singh
Solved On   : 11 Feb 2024
"""

from typing import List
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if n == 2: return sum(sum(g) for g in grid)
        elif n == 3: return sum(sum(g)-min(g) for g in grid)
        prev, dirs = [[0] * n for _ in range(n)], {(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)}
        for i in range(m - 1, -1, -1):
            curr = [[0] * n for _ in range(n)]
            for j in range(min(i + 1, n)):
                for k in range(max(j, n - i - 1), n):
                    for dir in dirs:
                        s, t = j + dir[0], k + dir[1]
                        if 0 <= s <= t < n and curr[j][k] < prev[s][t]:
                            curr[j][k] = prev[s][t]
                    curr[j][k] += grid[i][j] + (0 if j == k else grid[i][k])
            prev = curr
        return prev[0][-1]

# Time complexity: O(m * n ^ 3)
# Space complexity: O(n ^ 2)