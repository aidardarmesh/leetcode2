from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_diam = 0
        
        def max_depth(root):
            if not root:
                return 0
            
            left = max_depth(root.left)
            right = max_depth(root.right)
            
            self.max_diam = max(self.max_diam, left + right)
            
            return max(left, right) + 1
        
        max_depth(root)
        
        return self.max_diam
