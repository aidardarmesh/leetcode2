def route(graph, nodeA, nodeB):
    remaining = collections.deque()
    remaining.append(nodeA)
    visited = {nodeB}

    while remaining:
        node = remaining.popleft()

        if node == nodeB:
            return True
        
        for neigh in graph[nodeA]:
            if not neigh in visited:
                remaining.append(neigh)
                visited.add(neigh)

    return False
