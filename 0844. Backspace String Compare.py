from typing import *

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def render(s):
            deq = collections.deque()
            
            for c in s:
                if c == '#':
                    if deq:
                        deq.pop()
                else:
                    deq.append(c)
            
            return ''.join(deq)
        
        return render(S) == render(T)
