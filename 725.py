"""
Title       : 725. Split Linked List in Parts
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 6 Sept 2023
Solved Using    : Python3
"""

from typing import Optional, List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n, cur = 0, head
        while cur:
            n, cur = n + 1, cur.next
        q, r = divmod(n, k)
        res, cur = [], head
        for i in range(k):
            res.append(cur)
            for j in range(q + (i < r) - 1):
                if cur:
                    cur = cur.next
            if cur:
                cur.next, cur = None, cur.next
        return res + [None] * (k - len(res))

# Time Complexity  : O(n)
# Space Complexity : O(k)