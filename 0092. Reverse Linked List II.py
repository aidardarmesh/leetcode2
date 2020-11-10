from typing import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        sent = ListNode(-1)
        sent.next = head
        node = prev = sent
        
        for _ in range(m):
            prev = node
            node = node.next
        
        cur_head = node
        
        for _ in range(n-m):
            next_ = node.next
            node.next = next_.next
            next_.next = cur_head
            cur_head = next_
        
        prev.next = cur_head
        
        return sent.next
