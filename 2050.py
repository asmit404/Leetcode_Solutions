"""
Title       : 2050. Parallel Courses II
Difficulty  : Hard
Author      : Asmit Singh
Solved On   : 18 Oct 2023
Solved Using    : Python3
"""

from typing import List
from collections import deque

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[] for _ in range(n + 1)]
        indegree_counter = [0] * (n + 1)
        max_preq_time = [0] * (n + 1)
        for prev, curr in relations:
            graph[prev].append(curr)
            indegree_counter[curr] += 1

        queue, res = deque(course for course in range(1, n + 1) if not indegree_counter[course]), 0

        while queue:
            curr_course = queue.popleft()
            curr_time = max_preq_time[curr_course] + time[curr_course - 1]
            res = max(res, curr_time)
            for next_course in graph[curr_course]:
                max_preq_time[next_course] = max(
                    max_preq_time[next_course], curr_time)
                indegree_counter[next_course] -= 1
                if not indegree_counter[next_course]:
                    queue.append(next_course)
        return res

# Time Complexity  : O(n)
# Space Complexity : O(n)