"""
Title       : 1290. Convert Binary Number in a Linked List to Integer
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 3 Oct 2023
Solved Using    : Python3
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = 0
        while head:
            res = 2 * res + head.val
            head = head.next
        return res

# Time Complexity  : O(n)
# Space Complexity : O(1)