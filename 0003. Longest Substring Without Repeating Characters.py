from typing import *

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_idx = {}
        max_len = 0
        left_bound = -1
        
        for i in range(len(s)):
            if s[i] in char_idx:
                left_bound = char_idx[s[i]]
                new_char_idx = {}
                
                for char in char_idx:
                    if char_idx[char] >= left_bound:
                        new_char_idx[char] = char_idx[char]
                
                char_idx = new_char_idx
            char_idx[s[i]] = i
            max_len = max(max_len, i - left_bound)
        
        return max_len
