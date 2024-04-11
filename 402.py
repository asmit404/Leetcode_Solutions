"""
Title       : 402. Remove K Digits
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 11 Apr 2024
"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        pool = []
        if n == k: return '0'
        for i in range(n):
            while k > 0 and pool and pool[-1] > num[i]:
                pool.pop()
                k -= 1
            pool.append(num[i])

        res = "".join(pool[:-k]) if k > 0 else "".join(pool)
        res = res.lstrip('0')
        return res if res else '0'

# Time Complexity  : O(n)
# Space Complexity : O(n)