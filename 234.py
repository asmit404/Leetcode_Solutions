"""
Title       : 234. Palindrome Linked List
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 3 Oct 2023
Solved Using    : Python3
"""

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            curr, slow = slow, slow.next
            curr.next, prev = prev, curr

        while prev:
            if head.val != prev.val:
                return False
            head, prev = head.next, prev.next

        return True

# Time Complexity  : O(n)
# Space Complexity : O(1)