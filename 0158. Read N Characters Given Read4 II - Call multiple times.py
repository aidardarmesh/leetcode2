from typing import *

# The read4 API is already defined for you.
# def read4(buf: List[str]) -> int:

class Solution:
    def __init__(self):
        self.bp = 0
        self.buffer = ['']*4
        self.size = 0
    
    def read(self, buf: List[str], n: int) -> int:
        i = 0
        
        while i < n:
            if self.bp == self.size:
                self.bp = 0
                self.size = read4(self.buffer)
                
                if self.size == 0:
                    break
            
            buf[i] = self.buffer[self.bp]
            i += 1
            self.bp += 1
        
        return i
