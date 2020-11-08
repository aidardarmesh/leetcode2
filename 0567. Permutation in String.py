from typing import *

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def is_empty(d):
            for val in d.values():
                if val != 0:
                    return False
            return True
        
        cnt = collections.Counter(s1)
        left = 0
        
        for right in range(len(s2)):
            cnt[s2[right]] -= 1
        
            if right-left+1 > len(s1):
                cnt[s2[left]] += 1
                left += 1
            
            if is_empty(cnt):
                return True
        
        return False
