from typing import *

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def count(s):
            res = {}
            
            for c in s:
                if not c in res:
                    res[c] = 0
                else:
                    res[c] += 1
            
            return res
        
        s = count(s)
        t = count(t)
        
        if len(s) != len(t):
            return False
        
        for c in s:
            if not c in t or t[c] != s[c]:
                return False
        
        return True
