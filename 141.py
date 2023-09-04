"""
Title       : 141. Linked List Cycle
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 4 Sept 2023
Solved Using    : Python3
"""

from typing import Optional, ListNode
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: return True
        return False

# Time Complexity  : O(n)
# Space Complexity : O(1)