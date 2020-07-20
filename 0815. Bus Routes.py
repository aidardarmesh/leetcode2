from typing import *

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        
        from collections import deque, defaultdict
        
        routes = list(map(set, routes))
        graph = defaultdict(set)
        
        for bus_i, r1 in enumerate(routes):
            for bus_j in range(bus_i+1, len(routes)):
                r2 = routes[bus_j]
                
                if r1 & r2:
                    graph[bus_i].add(bus_j)
                    graph[bus_j].add(bus_i)
        
        seen, targets = set(), set()
        for bus_idx, route in enumerate(routes):
            if S in route:
                seen.add(bus_idx)
            
            if T in route:
                targets.add(bus_idx)
                
        deq = deque([(bus_idx, 1) for bus_idx in seen])
        
        while deq:
            bus_idx, depth = deq.popleft()
            
            if bus_idx in targets:
                return depth
            
            for next_bus_idx in graph[bus_idx]:
                if not next_bus_idx in seen:
                    seen.add(next_bus_idx)
                    deq.append((next_bus_idx, depth+1))
                    
        return -1
