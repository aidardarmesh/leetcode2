from typing import *

class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        
        return (A+A).find(B) != -1
