"""
Title       : 237. Delete Node in a Linked List
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 5 May 2024
"""

class Solution:
    def deleteNode(self, node):
        node.val, node.next = node.next.val, node.next.next

# Time Complexity  : O(1)
# Space Complexity : O(1)