from typing import *

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        max_len = 0
        cnt = {}
        left = -1
        k = 2
        
        for right in range(len(s)):
            cnt[s[right]] = cnt.get(s[right], 0) + 1
            
            while len(cnt) == k + 1:
                left += 1
                cnt[s[left]] -= 1
                
                if cnt[s[left]] == 0:
                    del cnt[s[left]]
            
            max_len = max(max_len, right-left)
        
        return max_len
