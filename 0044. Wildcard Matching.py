from typing import *

class Solution:
    def _remove_stars(self, p):
        ans = []
        was_last_star = False
        
        for char in p:
            if char == '*':
                if was_last_star:
                    continue
                else:
                    ans.append(char)
                    was_last_star = True
            else:
                ans.append(char)
                was_last_star = False
        
        return ''.join(ans)
    
    def _match(self, s, p):
        idx = (s,p)
        
        if idx in self.memo:
            return self.memo[idx]
        
        if p == s or p == '*':
            self.memo[idx] = True
        elif not p or not s:
            self.memo[idx] = False
        elif p[0] == s[0] or p[0] == '?':
            self.memo[idx] = self._match(s[1:], p[1:])
        elif p[0] == '*':
            self.memo[idx] = self._match(s[1:],p) or self._match(s,p[1:])
        else:
            self.memo[idx] = False
        
        return self.memo[idx]
        
    def isMatch(self, s: str, p: str) -> bool:
        p = self._remove_stars(p)
        self.memo = {}
        
        return self._match(s, p)
