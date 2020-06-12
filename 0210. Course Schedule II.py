from typing import *

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict
        
        graph = defaultdict(list)
        
        for u, v in prerequisites:
            graph[u].append(v)
            
        colors = {i:0 for i in range(numCourses)}
        
        def dfs_cycle(v, graph):
            colors[v] = 1
            
            for u in graph[v]:
                if colors[u] == 0:
                    if dfs_cycle(u, graph):
                        return True
                elif colors[u] == 1:
                    return True
            
            colors[v] = 2
            return False
        
        def has_cycle(graph, numCourses):
            for i in range(numCourses):
                if dfs_cycle(i, graph):
                    return True
        
        if has_cycle(graph, numCourses):
            return []
        
        def dfs(v, visited, stack, graph):
            if visited[v]:
                return
            
            visited[v] = True
            
            for u in graph[v]:
                dfs(u, visited, stack, graph)
            
            stack.append(v)
        
        stack = []
        visited = {i:False for i in range(numCourses)}
        
        for i in range(numCourses):
            dfs(i, visited, stack, graph)
        
        return stack
