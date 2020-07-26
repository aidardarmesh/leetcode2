from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float('-inf')
        
        def root_max_sum(root):
            if not root:
                return 0
            
            left = root_max_sum(root.left)
            right = root_max_sum(root.right)
            
            self.max_sum = max(self.max_sum, root.val, root.val + left, root.val + right, root.val + left + right)
            
            return max(root.val, root.val + left, root.val + right)
        
        root_max_sum(root)
        
        return self.max_sum
