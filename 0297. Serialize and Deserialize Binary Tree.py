from typing import *

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'None,'
        
        return str(root.val) + ',' + self.serialize(root.left) + self.serialize(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper(data):
            if not data:
                return None
            
            val = data.pop(0)
            node = TreeNode(val) if val != 'None' else None

            if data and node:
                node.left = helper(data)
            
            if data and node:
                node.right = helper(data)

            return node

        return helper(data.split(','))
