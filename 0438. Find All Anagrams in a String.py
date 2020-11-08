from typing import *

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # dealing with at most 26 symbols
        # therefore O(1)
        def is_empty(d):
            ans = True
            for val in d.values():
                if val != 0:
                    ans = False
            return ans
        
        res = []
        cnt = collections.Counter(p)
        left = 0
        
        for right in range(len(s)):
            cnt[s[right]] -= 1
            
            if right - left + 1 > len(p):
                cnt[s[left]] += 1
                left += 1
                
            if is_empty(cnt):
                res.append(left)
        
        return res
