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
        if self.memo.get((s,p)):
            return self.memo[(s,p)]
        
        if not p:
            return not s
        
        first_match = bool(s) and p[0] in {s[0], '?', '*'}
        
        if p and p[0] == '*':
            ans = self.isMatch(s, p[1:]) or first_match and self.isMatch(s[1:], p)
            self.memo[(s,p)] = ans
            return ans
        else:
            ans = first_match and self.isMatch(s[1:], p[1:])
            self.memo[(s,p)] = ans
            return ans
        
    def isMatch(self, s: str, p: str) -> bool:
        p = self._remove_stars(p)
        self.memo = {}
        
        return self._match(s, p)        
