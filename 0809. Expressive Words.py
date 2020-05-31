from typing import *

class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        from collections import deque
        
        def group(s):
            res = deque()
            res.append(['', 0])
            
            for c in s:
                if res[-1][0] == c:
                    res[-1][1] += 1
                else:
                    res.append([c, 1])
            
            res.popleft()
            
            return res
        
        S = group(S)
        
        def is_stretchy(word):
            word = group(word)
            
            if len(word) != len(S):
                return False
            
            for i in range(len(word)):
                if S[i][0] == word[i][0]:
                    if S[i][1] == word[i][1] or (S[i][1] >= 3 and S[i][1] > word[i][1]):
                        continue
                    else:
                        return False
                else:
                    return False
            
            return True
        
        res = [word for word in words if is_stretchy(word)]
        
        return len(res)
