from typing import *

class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        res = []
        idx_rep, idx_sources = {}, {}
        i = 0
        
        def check(S, substr, i):
            for char in substr:
                if char != S[i]:
                    return False
                i += 1
            
            return True
        
        for i in range(len(indexes)):
            idx = indexes[i]
            
            if check(S, sources[i], idx):
                idx_rep[idx] = targets[i]
                idx_sources[idx] = sources[i]
        
        i = 0
        
        while i < len(S):
            if i in idx_rep:
                res.append(idx_rep[i])
                i += len(idx_sources[i])
            else:
                res.append(S[i])
                i += 1
        
        return ''.join(res)
