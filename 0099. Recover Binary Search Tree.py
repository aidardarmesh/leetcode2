from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        x = y = pred = None
        node = root
        
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                
                if pred and node.val < pred.val:
                    y = node
                    
                    if not x:
                        x = pred
                    else:
                        break
                
                pred = node
                node = node.right
        
        x.val, y.val = y.val, x.val
