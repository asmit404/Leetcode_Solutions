"""
Title       : 1436. Destination City
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 15 Dec 2023
Solved Using    : Python3
"""

from typing import List
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start_cities, end_cities = zip(*paths)
        return (set(end_cities) - set(start_cities)).pop()

# Time Complexity  : O(n)
# Space Complexity : O(n)