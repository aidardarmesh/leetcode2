from typing import *

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        
        t = Counter(t)
        left = 0
        cnt = {}
        cand = ''
        
        def contains_all(cnt, t):
            for char in t:
                if not char in cnt:
                    return False
                
                if t[char] > cnt[char]:
                    return False
            
            return True
        
        for right in range(len(s)):
            if not s[right] in t:
                continue
            
            cnt[s[right]] = cnt.get(s[right], 0) + 1
            
            while contains_all(cnt, t):
                new_cand = s[left:right+1]
                
                if len(new_cand) < len(cand) or cand == '':
                    cand = new_cand
                
                if s[left] in cnt:
                    cnt[s[left]] -= 1
                    
                    if cnt[s[left]] == 0:
                        del cnt[s[left]]
            
                left += 1
        
        return cand
