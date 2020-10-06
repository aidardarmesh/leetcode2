from typing import *

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        ROWS = [set() for _ in range(n)]
        COLS = [set() for _ in range(n)]
        BOXES = [set() for _ in range(n)]
        EMPTY = []
        
        for i in range(n):
            for j in range(n):
                if board[i][j] == '.':
                    EMPTY.append((i,j))
                else:
                    int_val = int(board[i][j])
                    ROWS[i].add(int_val)
                    COLS[j].add(int_val)
                    BOXES[i//3*3 + j//3].add(int_val)
        
        def fits(val, r, c):
            return  (not val in ROWS[r]) and \
                    (not val in COLS[c]) and \
                    (not val in BOXES[r//3*3 + c//3])
        
        def setup(val, r, c):
            ROWS[r].add(val)
            COLS[c].add(val)
            BOXES[r//3*3 + c//3].add(val)
            board[r][c] = str(val)
            
        def remove(val, r, c):
            ROWS[r].remove(val)
            COLS[c].remove(val)
            BOXES[r//3*3 + c//3].remove(val)
            board[r][c] = '.'
        
        def backtrack(empty_id):
            if empty_id == len(EMPTY):
                return True
            
            r, c = EMPTY[empty_id]
            for val in range(1, n+1):
                if fits(val, r, c):
                    setup(val, r, c)
                    if backtrack(empty_id+1):
                        return True
                    remove(val, r, c)
        
        backtrack(0)
        
        return board
