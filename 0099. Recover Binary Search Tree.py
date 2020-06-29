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
        def in_order(node):
            return in_order(node.left) + [node.val] + in_order(node.right) if node else []
        
        def find_swapped(nums):
            x = y = -1
            
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    y = nums[i+1]
                    
                    if x == -1:
                        x = nums[i]
                    else:
                        break
            
            return x, y
        
        def recover(root, cnt):
            if root:
                if root.val == x or root.val == y:
                    root.val = y if root.val == x else x
                    cnt -= 1
                    
                    if cnt == 0:
                        return
                
                recover(root.left, cnt)
                recover(root.right, cnt)
        
        x, y = find_swapped(in_order(root))
        recover(root, 2)
