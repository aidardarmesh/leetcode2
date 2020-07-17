from typing import *

# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root:
            return ''
        
        from collections import deque
        
        deq = deque([root])
        res = [str(root.val), 'None']
        
        while deq:
            size = len(deq)
            
            for _ in range(size):
                node = deq.popleft()
                
                if node.children:
                    res += [str(child.val) for child in node.children]
                    deq += node.children
                res += ['None']
        
        return ','.join(res)
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return
        
        from collections import deque
        
        head = node = Node()
        data = deque(data.split(','))
        nodes = deque([node])
        
        while data:
            node = nodes.popleft()
            children = []
            
            while True:
                val = data.popleft()
                
                if val == 'None':
                    break
                
                child_node = Node(int(val))
                nodes.append(child_node)
                children.append(child_node)
            
            node.children = children
        
        return head.children[0]

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)
node10 = Node(10)
node11 = Node(11)
node12 = Node(12)
node13 = Node(13)
node14 = Node(14)
node1.children = [node2,node3,node4,node5]
node3.children = [node6,node7]
node4.children = [node8]
node5.children = [node9,node10]
node7.children = [node11]
node8.children = [node12]
node9.children = [node13]
node11.children = [node14]

c = Codec()
node1_ser = c.serialize(node1)
print(c.serialize(node1))
print(c.serialize(None))
