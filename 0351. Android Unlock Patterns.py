from typing import *

class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        res = 0
        dep = {
            (1,3): 2,
            (1,7): 4,
            (1,9): 5,
            (2,8): 5,
            (3,1): 2,
            (3,7): 5,
            (3,9): 6,
            (4,6): 5,
            (6,4): 5,
            (7,1): 4,
            (7,3): 5,
            (7,9): 8,
            (8,2): 5,
            (9,1): 5,
            (9,3): 6,
            (9,7): 8
        }
        
        def num_ways(curr, pushed, n):
            if len(pushed) == n:
                return 1
            
            res = 0
            
            for key in range(1, 10):
                if key in pushed:
                    continue
                
                if (curr,key) in dep and dep[(curr, key)] not in pushed:
                    continue
                
                pushed.add(key)
                res += num_ways(key, pushed, n)
                pushed.remove(key)
            
            return res
        
        for n_pushed in range(m, n+1):
            res += num_ways(0, set(), n_pushed)
        
        return res
