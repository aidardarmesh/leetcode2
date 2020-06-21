from typing import *

class Node:
	def __init__(self):
		self.children = {}
		self.is_end = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        
        for char in word:
            if not char in node.children:
                node.children[char] = Node()
            
            node = node.children[char]
        
        node.is_end = True

    def search(self, word: str, node=None) -> bool:
        if not node:
            node = self.root
        
        for i in range(len(word)):
            if word[i] == '.':
                for child in node.children.values():
                    if self.search(word[i+1:], child):
                        return True
			
            if not word[i] in node.children:
                return False
            
            node = node.children[word[i]]
        
        return node.is_end


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
