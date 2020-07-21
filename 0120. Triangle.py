from typing import *

class Solution:
    def minimumTotal(self, arr: List[List[int]]) -> int:
        if not arr:
            return 0
        
        ans = [arr[0][0]]
        
        for i in range(1, len(arr)):
            temp_ans = [float('inf')] * (len(ans)+1)
            
            for j in range(len(ans)):
                temp_ans[j] = min(temp_ans[j], ans[j]+arr[i][j])
                temp_ans[j+1] = min(temp_ans[j+1], ans[j]+arr[i][j+1])
            
            ans = temp_ans
        
        return min(ans)
