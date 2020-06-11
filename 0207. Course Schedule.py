from typing import *

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        
        graph = defaultdict(list)
        colors = defaultdict(int)
        
        for v, u in prerequisites:
            graph[v].append(u)
        
        def dfs(v):
            colors[v] = 1
            
            for u in graph[v]:
                if colors[u] == 0:
                    if dfs(u):
                        return True
                elif colors[u] == 1:
                    return True
            
            colors[v] = 2
            return False
        
        for v in range(numCourses):
            if dfs(v):
                return False
        
        for v in range(numCourses):
            if colors[v] != 2:
                return False
        
        return True
