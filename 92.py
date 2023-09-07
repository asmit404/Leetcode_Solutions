"""
Title       : 92. Reverse Linked List II
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 7 Sept 2023
Solved Using    : Python3
"""

from typing import Optional, ListNode
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        current = prev.next

        for _ in range(right - left):
            next_node = current.next
            current.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        return dummy.next

# Time Complexity  : O(n)
# Space Complexity : O(1)