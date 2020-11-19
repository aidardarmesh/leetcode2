from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root):
            if not root:
                return 0
            
            left = height(root.left)
            right = height(root.right)
            
            if abs(left-right) > 1:
                raise Exception()
            
            return max(left, right) + 1
        
        try:
            root_height = height(root)
        except:
            return False
        
        return True
