"""
Title       : 621. Task Scheduler
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 19 Mar 2024
"""

from typing import List
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_cnt = list(Counter(tasks).values())
        max_cnt = max(task_cnt)
        max_cnt_tasks = task_cnt.count(max_cnt)
        return max(len(tasks), (max_cnt - 1) * (n + 1) + max_cnt_tasks)

# Time Complexity  : O(n)
# Space Complexity : O(n)