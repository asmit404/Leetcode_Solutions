"""
Title       : 1095. Find in Mountain Array
Difficulty  : Hard
Author      : Asmit Singh
Solved On   : 12 Oct 2023
Solved Using    : Python3
"""

class Solution:
    def __init__(self):
        self.cache = dict()

    def peek(self, mountain_arr, i):
        if i not in self.cache:
            self.cache[i] = mountain_arr.get(i)
        return self.cache[i]

    def ternary_search(self, l, r, mountain_arr):
        while l < r:
            m1 = l + (r - l) // 3
            m2 = r - (r - l) // 3
            if self.peek(mountain_arr, m1) < self.peek(mountain_arr, m2):
                l = m1 + 1
            else:
                r = m2 - 1
        return l

    def binary_search_inc(self, l, r, target, mountain_arr):
        while l <= r:
            mid = (l + r) // 2
            if self.peek(mountain_arr, mid) < target:
                l = mid + 1
            elif self.peek(mountain_arr, mid) > target:
                r = mid - 1
            else:
                return mid
        return -1

    def binary_search_dec(self, l, r, target, mountain_arr):
        while l <= r:
            mid = (l + r) // 2
            if self.peek(mountain_arr, mid) > target:
                l = mid + 1
            elif self.peek(mountain_arr, mid) < target:
                r = mid - 1
            else:
                return mid
        return -1

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        peak = self.ternary_search(0, n - 1, mountain_arr)
        x = self.binary_search_inc(0, peak, target, mountain_arr)
        if x != -1:
            return x
        return self.binary_search_dec(peak + 1, n - 1, target, mountain_arr)

# Beat 100% submissions in runtime.
# Time Complexity  : O(log n)
# Space Complexity : O(n)