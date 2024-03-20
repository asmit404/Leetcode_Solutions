"""
Title       : 1669. Merge In Between Linked Lists
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 20 Mar 2024
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        pre = None
        cur = list1
        for _ in range(b + 1):
            if _ == a - 1:
                pre = cur
            cur = cur.next
        pre.next = list2
        while pre.next:
            pre = pre.next
        pre.next = cur
        return list1

# Time Complexity  : O(n)
# Space Complexity : O(1)