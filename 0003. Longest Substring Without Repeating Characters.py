from typing import *

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left = -1
        char_idx = {}
        
        for right in range(len(s)):
            if s[right] in char_idx:
                left = max(left, char_idx[s[right]])
            
            char_idx[s[right]] = right
            res = max(res, right-left)
        
        return res
