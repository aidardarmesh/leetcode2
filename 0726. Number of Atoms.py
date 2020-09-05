from typing import *

class Solution:
    def countOfAtoms(self, s: str) -> str:
        n = len(s)
        stack = [collections.defaultdict(int)]
        i = 0
        
        while i < n:
            if s[i] == '(':
                stack.append(collections.defaultdict(int))
                i += 1
            elif s[i] == ')':
                top = stack.pop()
                i += 1
                i_start = i
                
                while i < n and s[i].isdigit():
                    i += 1
                multi = int(s[i_start:i] or '1')
                
                for name, count in top.items():
                    stack[-1][name] += count * multi
            else:
                i_start = i
                i += 1
                
                while i < n and s[i].islower():
                    i += 1
                name = s[i_start:i]
                
                i_start = i
                while i < n and s[i].isdigit():
                    i += 1
                multi = int(s[i_start:i] or '1')
                
                stack[-1][name] += multi
        
        return ''.join(name + (str(stack[-1][name]) if stack[-1][name] > 1 else '') for name in sorted(stack[-1]))
