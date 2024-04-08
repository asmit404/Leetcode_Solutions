"""
Title       : 1700. Number of Students Unable to Eat Lunch
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 8 Apr 2024
"""

from typing import List
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt = 0
        while True:
            if len(students) == 0: return 0
            if len(students) == cnt: return cnt
            if students[0] == sandwiches[0]:
                cnt = 0
                students.pop(0)
                sandwiches.pop(0)
            else:
                cnt += 1
                students.append(students.pop(0))

# Time Complexity  : O(n ^ 2)
# Space Complexity : O(n)