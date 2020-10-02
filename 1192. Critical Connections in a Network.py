from typing import *

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict
        graph = defaultdict(list)
        for at, to in connections:
            graph[at].append(to)
            graph[to].append(at)
        
        n = len(graph)
        ids = [0 for _ in range(n)]
        visited = [False for _ in range(n)]
        low = [0 for _ in range(n)]
        bridges = []
        
        def dfs(at, parent, bridges):
            visited[at] = True
            ids[at] = low[at] = self.id
            self.id += 1
            
            for to in graph[at]:
                if to == parent:
                    continue
                    
                if not visited[to]:
                    dfs(to, at, bridges)
                    low[at] = min(low[at], low[to])
                    
                    if ids[at] < low[to]:
                        bridges.append([at,to])
                else:
                    low[at] = min(low[at], ids[to])
            
        self.id = 0
        for i in range(n):
            if not visited[i]:
                dfs(i, -1, bridges)
        
        return bridges
