from typing import *

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        self.circles = n
        uf = {i:i for i in range(n)}
        
        def find(v):
            if uf[v] == v:
                return v
            
            uf[v] = find(uf[v])
            
            return uf[v]
        
        def union(v, u):
            v_root = find(v)
            u_root = find(u)
            
            if v_root != u_root:
                self.circles -= 1
                uf[v_root] = u_root
        
        for i in range(n):
            for j in range(n):
                if M[i][j]:
                    if find(i) != find(j):
                        union(i,j)
        
        return self.circles
