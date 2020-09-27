from typing import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverse(head):
            sent = ListNode(-1)
            sent.next = head
            node = head

            while node and node.next:
                next_node = node.next
                node.next = next_node.next
                next_node.next = sent.next
                sent.next = next_node

            return sent.next
        
        l1 = reverse(l1)
        l2 = reverse(l2)
        l3 = node = ListNode(-1)
        quant = rem = 0
        
        while l1 and l2:
            nodes_sum = l1.val + l2.val + quant
            quant = nodes_sum // 10
            rem = nodes_sum % 10
            node.next = ListNode(rem)
            node = node.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            nodes_sum = l1.val + quant
            quant = nodes_sum // 10
            rem = nodes_sum % 10
            node.next = ListNode(rem)
            node = node.next
            l1 = l1.next
        
        while l2:
            nodes_sum = l2.val + quant
            quant = nodes_sum // 10
            rem = nodes_sum % 10
            node.next = ListNode(rem)
            node = node.next
            l2 = l2.next
        
        if quant:
            node.next = ListNode(quant)
        
        return reverse(l3.next)
