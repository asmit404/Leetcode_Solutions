"""
Title       : 141. Linked List Cycle
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 06 Mar 2024
"""

class Solution:
    def hasCycle(self, head) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: return True
        return False

# Time Complexity  : O(n)
# Space Complexity : O(1)