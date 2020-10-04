from typing import *

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        import copy
        
        rows = [True for _ in range(n)]
        cols = [True for _ in range(n)]
        hills = [True for _ in range(2*n-1)]
        valleys = [True for _ in range(2*n-1)]
        board = [['.' for _ in range(n)] for __ in range(n)]
        
        def occupy(r, c, val):
            rows[r] = val
            cols[c] = val
            hills[r+c] = val
            valleys[r-c+n-1] = val
        
        def render(board):
            board_copy = []
            
            for r in range(n):
                board_copy.append(''.join(board[r]))
            
            return board_copy
        
        def is_free(r, c):
            return rows[r] and \
                    cols[c] and \
                    hills[r+c] and \
                    valleys[r-c+n-1]
        
        def backtrack(r, board, res):
            if r == n:
                res.append(render(board))
                return
            
            for j in range(n):
                if is_free(r, j):
                    occupy(r, j, False)
                    board[r][j] = 'Q'
                    backtrack(r+1, board, res)
                    occupy(r, j, True)
                    board[r][j] = '.'
        
        res = []
        backtrack(0, board, res)
        
        return res
