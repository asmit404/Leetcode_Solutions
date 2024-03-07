"""
Title       : 876. Middle of the Linked List
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 07 Mar 2024
"""

class Solution(object):
    def middleNode(self, head):
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

# Time Complexity  : O(n)
# Space Complexity : O(1)