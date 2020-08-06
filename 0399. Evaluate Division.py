from typing import *

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        from collections import defaultdict, deque
        
        graph = defaultdict(list)
        
        for vertice, value in zip(equations, values):
            f, t = vertice
            graph[f].append((t, value))
            graph[t].append((f, 1/value))
        
        def bfs(query):
            start, end = query
            
            if not start in graph or not end in graph:
                return -1.0
            
            deq = deque([(start, 1.0)])
            visited = set()
            
            while deq:
                cur_node, cur_prod = deq.popleft()
                
                if cur_node == end:
                    return cur_prod
                
                for neighbor, cost in graph[cur_node]:
                    if not neighbor in visited:
                        deq.append((neighbor, cost * cur_prod))
                        visited.add(neighbor)
            
            return -1.0
        
        return [bfs(q) for q in queries]
