"""
Title       : 143. Reorder List
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 23 Mar 2024
"""

class Solution:
    def reorderList(self, head) -> None:
        if not head or not head.next or not head.next.next: return
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        prev, cur = None, slow.next
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        slow.next = None

        fHalf, sHalf = head, prev
        while fHalf and sHalf:
            fNext = fHalf.next
            sNext = sHalf.next
            fHalf.next = sHalf
            sHalf.next = fNext
            fHalf = fNext
            sHalf = sNext

# Time Complexity  : O(n)
# Space Complexity : O(1)