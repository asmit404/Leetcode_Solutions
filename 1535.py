"""
Title       : 1535. Find the Winner of an Array Game
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 05 Nov 2023
Solved Using    : Python3
"""

class Solution:
    def getWinner(self, arr, k):
        winner, count = arr[0], 0
        for num in arr[1:]:
            if num > winner:
                winner = num
                count = 1
            else:
                count += 1
            if count == k:
                return winner
        return winner

# Time Complexity  : O(n)
# Space Complexity : O(1)