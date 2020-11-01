from typing import *

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_ = 0
        memo = {}
        
        def square(matrix, i, j, memo):
            if (i,j) in memo:
                return memo[(i,j)]
            
            if i == len(matrix) or j == len(matrix[0]):
                return 0
            
            if matrix[i][j] == '0':
                return 0
            
            memo[(i,j)] = 1 + min([
                square(matrix, i, j+1, memo),
                square(matrix, i+1, j, memo),
                square(matrix, i+1, j+1, memo),
            ])
            
            return memo[(i,j)]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    max_ = max(max_, square(matrix, i, j, memo))
        
        return max_ ** 2
