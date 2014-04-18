"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example, Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head:
            p = head
            while p.next != None:
                if p.next.val != p.val:
                    p = p.next
                else:
                    p.next = p.next.next
        return head  