from typing import *

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        memo = [[-1 for _ in range(len(s2)+1)] for __ in range(len(s1)+1)]
        
        def concat(s1, s2, s3, i, j, k, memo):
            if memo[i][j] >= 0:
                return True if memo[i][j] == 1 else False
            
            if i == len(s1) and j == len(s2) and k == len(s3):
                return True
            
            ans = False
            
            if i < len(s1) and s1[i] == s3[k]:
                ans |= concat(s1, s2, s3, i+1, j, k+1, memo)
            
            if j < len(s2) and s2[j] == s3[k]:
                ans |= concat(s1, s2, s3, i, j+1, k+1, memo)
            
            memo[i][j] = 1 if ans else 0
            
            return ans
        
        return concat(s1, s2, s3, 0, 0, 0, memo)
