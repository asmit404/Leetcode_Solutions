"""
Title       : 135. Candy
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 13 Sept 2023
Solved Using    : Python3
"""

class Solution:
    def candy(self, ratings):
        number = len(ratings)
        candies = [1] * number

        for i in range(1, number):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1

        for i in range(number-2, -1, -1):
            if ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
                candies[i] = candies[i+1] + 1

        return sum(candies)

# Time Complexity  : O(n)
# Space Complexity : O(1)