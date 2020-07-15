from typing import *

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left, max_len = -1, 0
        
        for right in range(len(A)):
            if A[right] == 0:
                K -= 1
            
            while K < 0:
                left += 1
                
                if A[left] == 0:
                    K += 1
            
            max_len = max(max_len, right-left)
        
        return max_len
