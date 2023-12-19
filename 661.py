"""
Title       : 661. Image Smoother
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 19 Dec 2023
Solved Using    : Python3
"""

from typing import List
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        L = len(img)
        W = len(img[0])
        prefix_sum = [[0] * (W + 1) for _ in range(L + 1)]

        for i in range(L):
            for j in range(W):
                prefix_sum[i + 1][j + 1] = img[i][j] + prefix_sum[i][j + 1] + prefix_sum[i + 1][j] - prefix_sum[i][j]

        result = [[0] * W for _ in range(L)]
        x1 = [max(i - 1, 0) for i in range(L)]
        y1 = [max(j - 1, 0) for j in range(W)]
        x2 = [min(i + 1, L - 1) for i in range(L)]
        y2 = [min(j + 1, W - 1) for j in range(W)]

        for i in range(L):
            for j in range(W):
                count = (x2[i] - x1[i] + 1) * (y2[j] - y1[j] + 1)
                total = prefix_sum[x2[i] + 1][y2[j] + 1] - prefix_sum[x1[i]][y2[j] + 1] - prefix_sum[x2[i] + 1][y1[j]] + prefix_sum[x1[i]][y1[j]]
                result[i][j] = int(total / count)

        return result

# Time Complexity  : O(n * m)
# Space Complexity : O(n * m)