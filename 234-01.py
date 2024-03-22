"""
Title       : 234. Palindrome Linked List
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 22 Mar 2024
"""

class Solution:
    def isPalindrome(self, head) -> bool:
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev

# Time Complexity  : O(n)
# Space Complexity : O(1)