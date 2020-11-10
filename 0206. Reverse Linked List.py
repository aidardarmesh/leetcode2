from typing import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        sent = ListNode(-1)
        sent.next = head
        curr = head
        
        while curr and curr.next:
            next_ = curr.next
            curr.next = next_.next
            next_.next = sent.next
            sent.next = next_
        
        return sent.next
