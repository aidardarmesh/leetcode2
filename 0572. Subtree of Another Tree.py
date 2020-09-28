from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def isMatch(s, t):
            if s and not t:
                return False
            
            if not s and t:
                return False
            
            if not s and not t:
                return True

            if s.val == t.val:
                if isMatch(s.left, t.left) and isMatch(s.right, t.right):
                    return True
            
            return False
        
        if isMatch(s, t):
            return True
        
        if s is None:
            return False
        
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
