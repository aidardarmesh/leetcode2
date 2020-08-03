from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        def compare(x,y):
            if not x and not y:
                return True
            
            if (not x and y) or (x and not y):
                return False
            
            if x.val != y.val:
                return False
            
            straight = compare(x.left, y.left) and compare(x.right, y.right)
            flipped = compare(x.left, y.right) and compare(x.right, y.left)
            
            return straight or flipped
        
        return compare(root1, root2)
