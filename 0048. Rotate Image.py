from typing import *

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        
        for i in range(n):
            for j in range(m//2):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(n):
            for j in range(m//2):
                matrix[i][j], matrix[i][m-1-j] = matrix[i][m-1-j], matrix[i][j]

s = Solution()
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
s.rotate(matrix)
print(matrix)