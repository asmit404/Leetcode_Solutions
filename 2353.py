"""
Title       : 2353. Design a Food Rating System
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 17 Dec 2023
Solved Using    : Python3
"""

import heapq
from typing import List
from collections import defaultdict

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_to = {}
        self.cuisine_to = defaultdict(list)
        for food, rating, cuisine in zip(foods, ratings, cuisines):
            heapq.heappush(self.cuisine_to[cuisine], (-rating, food))
            self.food_to[food] = (rating, cuisine)

    def changeRating(self, food: str, newRating: int) -> None:
        prev_rating, prev_cuisine = self.food_to[food]
        heapq.heappush(self.cuisine_to[prev_cuisine], (-newRating, food))
        self.food_to[food] = (newRating, prev_cuisine)

    def highestRated(self, cuisine: str) -> str:
        curr_heap = self.cuisine_to[cuisine]
        while curr_heap and -self.food_to[curr_heap[0][1]][0] != curr_heap[0][0]:
            heapq.heappop(curr_heap)
        return curr_heap[0][1] if curr_heap else None

# Nice question. Almost had to use my brain.
# Time Complexity  : O(n)
# Space Complexity : O(n)