from typing import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def merge(l1, l2):
            res = head = ListNode(-1)
            
            while l1 and l2:
                if l1.val < l2.val:
                    res.next = l1
                    res = res.next
                    l1 = l1.next
                else:
                    res.next = l2
                    res = res.next
                    l2 = l2.next
            
            if l1:
                res.next = l1
            
            if l2:
                res.next = l2
            
            return head.next
        
        n_lists = len(lists)
        delta = 1
        
        while delta < n_lists:
            for i in range(0, n_lists - delta, delta * 2):
                lists[i] = merge(lists[i], lists[i+delta])
            
            delta *= 2
        
        return lists[0] if n_lists else None
