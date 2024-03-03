"""
Title       : 19. Remove Nth Node From End of List
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 03 Mar 2024
"""

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n: int):
        slow = fast = head
        while n > 0:
            fast = fast.next
            n -= 1
        if not fast: return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

# Time Complexity: O(n)
# Space Complexity: O(1)