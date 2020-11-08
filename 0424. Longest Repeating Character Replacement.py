from typing import *

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        res = maxf = 0
        cnt = defaultdict(int)
        left = 0
        
        for right in range(len(s)):
            cnt[s[right]] += 1
            maxf = max(maxf, cnt[s[right]])
            
            while right - left + 1 - maxf > k:
                cnt[s[left]] -= 1
                left += 1
            
            res = max(res, right-left+1)
        
        return res
