from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        
        if not root:
            return res
        
        queue = collections.deque()
        queue.append(root)
        level = 1
        while queue:
            size = len(queue)
            level_data = collections.deque()
            is_odd = level % 2 == 1
            for _ in range(size):
                node = queue.popleft()
                
                if is_odd:
                    level_data.append(node.val)
                else:
                    level_data.appendleft(node.val)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            res.append(level_data)
            level += 1
        
        return res
