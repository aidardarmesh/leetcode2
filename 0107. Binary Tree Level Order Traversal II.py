from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        res = collections.deque()
        deq = collections.deque()
        deq.append(root)
        
        while deq:
            size = len(deq)
            level = []
            
            for _ in range(size):
                node = deq.popleft()
                level.append(node.val)
                
                if node.left:
                    deq.append(node.left)
                
                if node.right:
                    deq.append(node.right)
            
            res.appendleft(level)
        
        return res
