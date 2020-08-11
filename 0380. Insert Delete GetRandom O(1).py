from typing import *

import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.indices:
            return False
        
        self.data.append(val)
        self.indices[val] = len(self.data)-1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if not val in self.indices:
            return False
        
        removed_elem_idx = self.indices[val]
        last_elem = self.data[-1]
        self.indices[last_elem] = removed_elem_idx
        del self.indices[val]
        self.data[removed_elem_idx], self.data[-1] = self.data[-1], self.data[removed_elem_idx]
        self.data.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.data)

