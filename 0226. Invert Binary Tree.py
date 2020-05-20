from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        
        stack = [root]
        
        while stack:
            node = stack.pop()
            
            if node.right:
                stack.append(node.right)
            
            if node.left:
                stack.append(node.left)
                
            node.left, node.right = node.right, node.left
        
        return root
