from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        if not root:
            return res
        
        def helper(node, vals, curr_sum, _sum, res):
            if not node:
                return
            
            curr_sum += node.val
            vals.append(node.val)
            
            if curr_sum == _sum and not node.left and not node.right:
                res.append(vals[:])
            
            helper(node.left, vals, curr_sum, _sum, res)
            helper(node.right, vals, curr_sum, _sum, res)
            
            vals.pop()
        
        helper(root, [], 0, sum, res)
        
        return res
