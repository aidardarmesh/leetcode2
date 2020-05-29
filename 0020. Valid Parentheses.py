from typing import *

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        open_brackets = set(brackets.values())
        
        for char in s:
            if char in open_brackets:
                stack.append(char)
            else:
                
                if not stack or not char in brackets or brackets[char] != stack.pop():
                    return False
        
        if stack:
            return False
        
        return True
