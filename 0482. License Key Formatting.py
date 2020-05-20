from typing import *

class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        stack = []
        separator = '-'
        chunk = 0
        
        for i in range(len(S)-1, -1, -1):
            if S[i] == separator:
                continue
            
            if 'a' <= S[i] <= 'z':
                stack.append(chr(ord(S[i])-32))
            else:
                stack.append(S[i])
            
            chunk += 1
            
            if chunk == K:
                stack.append(separator)
                chunk = 0
        
        if stack and stack[-1] == separator:
            stack.pop()
        
        return ''.join(stack[::-1])
