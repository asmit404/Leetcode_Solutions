"""
Title       : 1171. Remove Zero Sum Consecutive Nodes from Linked List
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 12 Mar 2024
"""

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = curr = ListNode(0, head)
        pool = {0: front}
        prefix_sum = 0

        while curr:
            prefix_sum += curr.val
            pool[prefix_sum] = curr
            curr = curr.next

        prefix_sum = 0
        curr = front
        while curr:
            prefix_sum += curr.val
            curr.next = pool[prefix_sum].next
            curr = curr.next
        return front.next

# Time Complexity  : O(n)
# Space Complexity : O(n)