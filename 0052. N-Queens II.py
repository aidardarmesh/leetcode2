from typing import *

class Solution:
    def totalNQueens(self, n: int) -> int:
        import copy
        
        rows = [True for _ in range(n)]
        cols = [True for _ in range(n)]
        hills = [True for _ in range(2*n-1)]
        valleys = [True for _ in range(2*n-1)]
        self.res = 0
        
        def occupy(r, c, val):
            rows[r] = val
            cols[c] = val
            hills[r+c] = val
            valleys[r-c+n-1] = val
        
        def is_free(r, c):
            return rows[r] and \
                    cols[c] and \
                    hills[r+c] and \
                    valleys[r-c+n-1]
        
        def backtrack(r):
            if r == n:
                self.res += 1
                return
            
            for j in range(n):
                if is_free(r, j):
                    occupy(r, j, False)
                    backtrack(r+1)
                    occupy(r, j, True)
        
        backtrack(0)
        
        return self.res
