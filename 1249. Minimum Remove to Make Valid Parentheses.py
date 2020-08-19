from typing import *

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        BRACKETS = {'(', ')'}
        
        def valid_brackets(s):
            open, closed = [], []
            
            for i, char in enumerate(s):
                if char == '(':
                    open.append(i)
                elif char == ')':
                    if len(closed) < len(open):
                        closed.append(i)
            
            for _ in range(len(open)-len(closed)):
                open.pop()
            
            import heapq
            
            heap = []
            while open or closed:
                if open:
                    heapq.heappush(heap, open.pop())
                
                if closed:
                    heapq.heappush(heap, closed.pop())
            
            return heap
        
        brackets = valid_brackets(s)
        
        temp_s = []
        for i, char in enumerate(s):
            if char in BRACKETS:
                if brackets and i == brackets[0]:
                    temp_s.append(char)
                    heapq.heappop(brackets)
            else:
                temp_s.append(char)
        
        return ''.join(temp_s)
