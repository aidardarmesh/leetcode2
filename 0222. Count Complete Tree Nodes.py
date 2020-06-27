from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        from collections import deque
        
        deq, cnt = deque(), 0
        
        if root:
            deq.append(root)
        
        while deq:
            size = len(deq)
            
            for _ in range(size):
                node = deq.popleft()
                cnt += 1
                
                if node.left:
                    deq.append(node.left)
                
                if node.right:
                    deq.append(node.right)
            
        return cnt
