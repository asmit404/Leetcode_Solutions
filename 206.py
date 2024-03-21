"""
Title       : 206. Reverse Linked List
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 21 Mar 2024
"""

class Solution:
    def reverseList(self, head):
        prev, cur = None, head
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev

# Time Complexity  : O(n)
# Space Complexity : O(1)