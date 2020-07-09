from typing import *

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        from collections import deque
        
        deq = deque()
        deq.append(root)
        res = []
        
        while deq:
            level = []
            size = len(deq)
            
            for _ in range(size):
                node = deq.popleft()
                level.append(node.val)
                deq += node.children
            
            res.append(level)
        
        return res
