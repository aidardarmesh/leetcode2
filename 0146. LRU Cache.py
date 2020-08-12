from typing import *

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.data = {}  # key: Node(val)
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.right = self.tail
        self.tail.left = self.head

    def _top(self, node):
        if node.left and node.right:
            node.left.right = node.right
            node.right.left = node.left
        
        first_node = self.head.right
        node.right = first_node
        first_node.left = node
        self.head.right = node
        node.left = self.head
    
    def _pop(self):
        if self.size > 0:
            last_node = self.tail.left
            del self.data[last_node.key]
            self.tail.left = last_node.left
            last_node.left.right = self.tail
    
    def get(self, key: int) -> int:
        if not key in self.data:
            return -1
        
        node = self.data[key]
        self._top(node)
        
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            node = self.data[key]
            node.val = value
            self._top(node)
        else:
            node = Node(key, value)
            self.data[key] = node
            self._top(node)
            self.size += 1
            
            if self.size > self.cap:
                self._pop()
                self.size -= 1

